#!/usr/bin/env python3
"""
Live Telemetry Metric Simulator for DevOps Assignment 2
Streams simulated CPU, Memory, Network, Uptime, and HTTP response metrics to Graphite.
Run this script while taking screenshots of Graphite and Grafana!
"""

import socket
import time
import random

CARBON_SERVER = 'localhost'
CARBON_PORT = 2003

def send_metric(sock, metric_path, value, timestamp):
    message = f"{metric_path} {value} {timestamp}\n"
    sock.sendall(message.encode('utf-8'))

def main():
    print(f"Connecting to Graphite Carbon at {CARBON_SERVER}:{CARBON_PORT}...")
    try:
        sock = socket.socket()
        sock.connect((CARBON_SERVER, CARBON_PORT))
        print("✔ Connected successfully! Streaming metrics every 3 seconds...")
        print("Press Ctrl+C to stop streaming.\n")
    except Exception as e:
        print(f"❌ Could not connect to Graphite on port {CARBON_PORT}. Make sure docker-compose is running!")
        print(f"Error: {e}")
        return

    uptime = 86400  # Start at 24 hours uptime in seconds
    try:
        while True:
            now = int(time.time())
            
            # Simulate realistic fluctuating server metrics
            cpu_usage = round(random.uniform(18.5, 38.2), 2)
            memory_usage = round(random.uniform(52.0, 64.5), 2)
            disk_usage = 42.1
            network_rx = round(random.uniform(120.0, 450.0), 2)
            network_tx = round(random.uniform(80.0, 310.0), 2)
            http_availability = 100.0
            http_response_time_ms = round(random.uniform(3.2, 7.8), 2)
            uptime += 3

            # Send metrics to Graphite path: devops.servers.production.*
            send_metric(sock, "devops.servers.production.cpu.usage", cpu_usage, now)
            send_metric(sock, "devops.servers.production.memory.usage", memory_usage, now)
            send_metric(sock, "devops.servers.production.disk.usage", disk_usage, now)
            send_metric(sock, "devops.servers.production.network.rx_kbps", network_rx, now)
            send_metric(sock, "devops.servers.production.network.tx_kbps", network_tx, now)
            send_metric(sock, "devops.servers.production.http.availability", http_availability, now)
            send_metric(sock, "devops.servers.production.http.latency_ms", http_response_time_ms, now)
            send_metric(sock, "devops.servers.production.uptime_seconds", uptime, now)

            print(f"[{time.strftime('%H:%M:%S')}] Transmitted metrics -> CPU: {cpu_usage}% | Mem: {memory_usage}% | Latency: {http_response_time_ms}ms")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nStopped metric simulation.")
    finally:
        sock.close()

if __name__ == '__main__':
    main()
