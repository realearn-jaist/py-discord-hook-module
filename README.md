## py-discord-hook
A self-implemented discord bot python module based on [[discord.py]](https://github.com/Rapptz/discord.py) for easy bot message to your server. This module was tailor-made to notify me when my machine learning training task finished and to keep a log of the results; that's why the functions are still limited to these tasks.
## Setup
**Prerequisite**
- Python 3.7 or higher

To install the module, you can clone this repository then navigate to the downloaded folder (*in your shell/cmd*) and run the following command:

    # Install required libraries
    pip install -r requirements.txt
    
    #Install py-discord-hook
    pip install .
    
   ## How to use
To use this module, you need a server in discord and acquire your webhook link to use this module.
> *refer to https://docs.gitlab.com/ee/user/project/integrations/discord_notifications.html*

After you get your webhook link, you can put it in the **savedURL.yaml** file to use it in your python code.
The **savedURL.yaml** will be in the installed directory of this module. You can change your **savedURL.yaml** file path via **config.cfg**

## Example

    from discordHook import discordApp
	
	discord = discordApp(url='Your webhook URL')
	#Or you can use
	#discord = discordApp(savedName='Your saved webhook name in savedURL.yaml')
	
	#To test if your module work or not
	discord.test()
	
	#To send message
	#PARAMETER
	#message (str) : the message that will be sent
	#mention (str) : the @ mention in discord for mare specific discord notification you can also use ['everyone', 'all'] for '@everyone'
	#log (T/F) : change whether the log will be kept or not
	discord.send(message='Some message', mention='user in your server', log=True)
	
	#If you have arguments parameter, you can send it via
	discord.send_arg(FLAGS=Your_args_param)
