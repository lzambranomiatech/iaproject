#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa para búsqueda de IP según nombre de servidor
Lee un archivo CSV con nombres de servidores y resuelve sus direcciones IP
"""

import socket
import csv
import sys
import argparse
from typing import List, Dict, Optional


def resolver_ip(hostname: str) -> Optional[str]:
    """
    Resuelve la dirección IP de un hostname.
    
    Args:
        hostname: Nombre del servidor a resolver
        
    Returns:
        Dirección IP o None si no se puede resolver
    """
    try:
        # Intenta resolver el hostname a IPv4
        ip = socket.gethostbyname(hostname.strip())
        return ip
    except socket.gaierror:
        # Error de resolución DNS
        return None
    except Exception as e:
        print(f"Error al resolver {hostname}: {e}", file=sys.stderr)
        return None


def resolver_ips_multiples(hostnames: List[str]) -> List[Dict[str, str]]:
    """
    Resuelve las direcciones IP de múltiples hostnames.
    
    Args:
        hostnames: Lista de nombres de servidores
        
    Returns:
        Lista de diccionarios con 'servidor' e 'ip'
    """
    resultados = []
    for hostname in hostnames:
        if not hostname or not hostname.strip():
            continue
            
        ip = resolver_ip(hostname)
        resultados.append({
            'servidor': hostname.strip(),
            'ip': ip if ip else 'NO_RESUELTO'
        })
    
    return resultados


def leer_csv_servidores(archivo_csv: str) -> List[str]:
    """
    Lee un archivo CSV y extrae los nombres de servidores.
    Asume que los servidores están en la primera columna o en una columna llamada 'servidor'/'server'/'hostname'.
    
    Args:
        archivo_csv: Ruta al archivo CSV
        
    Returns:
        Lista de nombres de servidores
    """
    servidores = []
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as f:
            # Intentar detectar si tiene encabezado
            primera_linea = f.readline()
            f.seek(0)
            
            reader = csv.DictReader(f)
            
            # Verificar si tiene encabezado con nombres conocidos
            if reader.fieldnames:
                posibles_columnas = ['servidor', 'server', 'hostname', 'host', 'nombre']
                columna_servidor = None
                
                for col in posibles_columnas:
                    if col in [c.lower() for c in reader.fieldnames]:
                        columna_servidor = col
                        # Encontrar el nombre real de la columna (con mayúsculas)
                        for campo in reader.fieldnames:
                            if campo.lower() == col:
                                columna_servidor = campo
                                break
                        break
                
                if columna_servidor:
                    # Usar la columna específica
                    for row in reader:
                        if row[columna_servidor] and row[columna_servidor].strip():
                            servidores.append(row[columna_servidor].strip())
                else:
                    # Usar la primera columna
                    primera_col = reader.fieldnames[0]
                    for row in reader:
                        if row[primera_col] and row[primera_col].strip():
                            servidores.append(row[primera_col].strip())
            else:
                # CSV sin encabezado, leer la primera columna
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0].strip():
                        servidores.append(row[0].strip())
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_csv}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}", file=sys.stderr)
        sys.exit(1)
    
    return servidores


def guardar_resultados_csv(resultados: List[Dict[str, str]], archivo_salida: str):
    """
    Guarda los resultados en un archivo CSV.
    
    Args:
        resultados: Lista de diccionarios con 'servidor' e 'ip'
        archivo_salida: Ruta del archivo de salida
    """
    try:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['servidor', 'ip'])
            writer.writeheader()
            writer.writerows(resultados)
        print(f"\nResultados guardados en: {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar resultados: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Busca direcciones IP de servidores desde un archivo CSV',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python busquedaip.py servidores.csv
  python busquedaip.py servidores.csv -o resultados.csv
  python busquedaip.py servidores.csv --output resultados.csv
        """
    )
    
    parser.add_argument(
        'archivo_csv',
        help='Archivo CSV con la lista de nombres de servidores'
    )
    
    parser.add_argument(
        '-o', '--output',
        dest='archivo_salida',
        help='Archivo CSV de salida con los resultados (opcional)'
    )
    
    args = parser.parse_args()
    
    # Leer servidores del CSV
    print(f"Leyendo servidores desde: {args.archivo_csv}")
    servidores = leer_csv_servidores(args.archivo_csv)
    
    if not servidores:
        print("No se encontraron servidores en el archivo CSV.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Se encontraron {len(servidores)} servidor(es) para resolver.\n")
    
    # Resolver IPs
    print("Resolviendo direcciones IP...")
    resultados = resolver_ips_multiples(servidores)
    
    # Mostrar resultados
    print("\n" + "="*60)
    print(f"{'Servidor':<40} {'IP':<20}")
    print("="*60)
    
    resueltos = 0
    no_resueltos = 0
    
    for resultado in resultados:
        servidor = resultado['servidor']
        ip = resultado['ip']
        
        if ip == 'NO_RESUELTO':
            print(f"{servidor:<40} {'NO_RESUELTO':<20}")
            no_resueltos += 1
        else:
            print(f"{servidor:<40} {ip:<20}")
            resueltos += 1
    
    print("="*60)
    print(f"\nResumen: {resueltos} resueltos, {no_resueltos} no resueltos")
    
    # Guardar resultados si se especificó archivo de salida
    if args.archivo_salida:
        guardar_resultados_csv(resultados, args.archivo_salida)


if __name__ == '__main__':
    main()

