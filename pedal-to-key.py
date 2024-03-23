import rtmidi
import mido
import keyboard

class PedalToKey:
    def list_midi_devices(self):
        midi_in = rtmidi.MidiIn()
        available_ports = midi_in.get_ports()
        # Raise assertion error if no device exists
        assert len(available_ports) > 0
        devices = enumerate(available_ports)
        print("Available MIDI input devices:")
        for i, port_name in devices:
                print(f"{i}. {port_name}")
        choosed_device = int(input('Choose your device: '))
        # choosed_device = 0
        # For loop empties the enumerate object so we cannot use our previously created object 'devices'
        self.device_name = dict(enumerate(available_ports))[choosed_device]
    def convert_midi_input(self, key_to_press='space'):
        try:
            with mido.open_input(self.device_name) as port:
                for msg in port:
                    # My pedal sends the value 127 when it is pressed and 0 when it is released
                    # I have neither worked with any other pedals nor I have any knowledge about
                    # them so feel free to change these values based on your hardware. Printing
                    # msg should show you every MIDI input with its data 
                    if 'value=127' in str(msg):
                        keyboard.press(key_to_press) 
                    if 'value=0' in str(msg):
                        keyboard.release(key_to_press)
        except OSError as o:
            print(f"Error opening MIDI input device: {self.device_name}\n{o}")

if __name__ == '__main__':
    main = PedalToKey()
    main.list_midi_devices()
    main.convert_midi_input()