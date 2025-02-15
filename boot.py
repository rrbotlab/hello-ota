import gc
import machine
import network

def main():
    """Main function. Runs after board boot, before main.py
    Connects to Wi-Fi and checks for latest OTA version.
    """

    gc.collect()
    gc.enable()

    import senko
    OTA = senko.Senko(branch='main', url='https://raw.githubusercontent.com/rrbotlab/hello-ota/main', user="rrbotlab", repo="hello-ota", working_dir="", files=["hello_ota.py"])

    print('\n\n\nChecking for updates...')
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()


if __name__ == "__main__":
    main()
