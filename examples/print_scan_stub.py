from create3_lidar_client import ScanClient


def on_scan(msg):
    # Ejemplo mínimo: imprime el número de lecturas y el ángulo inicial
    print(len(msg.ranges), msg.angle_min)


def main():
    client = ScanClient()
    client.start(on_scan)
    client.spin()


if __name__ == "__main__":
    main()
