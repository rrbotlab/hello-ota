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
    # OTA = senko.Senko(branch='main', url='https://raw.githubusercontent.com/rrbotlab/hello-ota/main', user="rrbotlab", repo="hello-ota", working_dir="", files=["hello_ota.py"])
    OTA = senko.Senko(branch='rr-tests', user='rrbotlab', repo='hello-ota', files=['hello_ota.py'])

    print('\n\n\nChecking for updates...', OTA.base_url, OTA.url)
    if OTA.update():
        print('Updated to the latest version!')
        input('press any key to reboot...')
        machine.reset()


if __name__ == '__main__':
    main()
