import serial
import serial.tools.list_ports

def humidity_percent(inputs):
    print(inputs)
    try:
        media = sum(inputs)//len(inputs)
        sensor_percent = 100 - ((media/1023) * 100)
    except ZeroDivisionError:
        sensor_percent = 0
    
    return sensor_percent

for port in serial.tools.list_ports.comports():
    if 'usb' in str(port):
        serial_port = str(port)

try:
    ser = serial.Serial(serial_port.split(' - ')[0])
except NameError:
    print('Dispositivo Offline')

with ser as serial_monitor:
    while True:
        reads = 1

        while reads <= 5:
            inputs = {
                1: list(),
                2: list(),
                3: list(),
                4: list(),
                5: list()
            }
            try:
                value = serial_monitor.readline().decode().strip()
                for key, sensor in enumerate(value.split(','), start=1):
                    inputs[key].append(int(sensor))

            except UnicodeDecodeError:
                pass
            except IndexError:
                pass
            except serial.serialutil.SerialException:
                print('A conexão caiu.')

            reads += 1
        
        for key, value in inputs.items():
            inputs[key] = humidity_percent(value)
        
        print(f'Manjericão: {inputs[1]:.2f}%')
        print(f'Hortelã: {inputs[2]:.2f}%')
        print(f'Manjerona: {inputs[3]:.2f}%')
        print(f'Tomate: {inputs[4]:.2f}%')
        print(f'Flor: {inputs[5]:.2f}%')
        print()
