from VL1.VL1 import VL1

try:
    with VL1() as bot:
        bot.land_first_page()
        bot.scroll_to_bottom()
        bot.go_to_top()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows CMD: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Windows Powershell: \n'
            '    $env:Path += ";C:path-to-your-folder \n'
            'E.g: \n'
            '     $env:Path += ";C:\\SeleniumDrivers\\" \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/to-your/folder/ \n'
        )
    else:
        raise
