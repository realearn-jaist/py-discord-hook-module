from discord import SyncWebhook
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import configparser
import yaml
import inspect
import os


"""
@Chavakan 1.0.0 2023-8-2
"""
class discordApp:
    def __init__(self, url: str = None, savedName: str = None, progName:str = None):
        
        self._progName = progName if progName != None else inspect.stack()[1].filename 

        _path = os.path.dirname(__file__)
        """ Set up the file path for all the files """
        self._config = configparser.ConfigParser()
        self._config_file = os.path.join(_path,'config.cfg')
        self._config.read(self._config_file)
        self._LOG_PATH = os.path.join(_path,'log_file') if self._config['FILEPATH']['log_path'].lower() == 'default' else os.path.join(self._config['FILEPATH']['log_path'],'log_file')
        self._URL_PATH = os.path.join(_path,'savedURL.yaml') if self._config['FILEPATH']['url_path'].lower() == 'default' else os.path.join(self._config['FILEPATH']['url_path'],'savedURL.yaml')
        self._prompt = self._config['PARAMETERS']['prompt'].lower()

        """ Connect to the discord webhook """
        with open(self._URL_PATH, 'r') as f:
            self._savedURL = yaml.safe_load(f)

        self._savedURL = {k.lower(): v for k, v in self._savedURL.items()}
        if savedName != None and savedName.lower() in self._savedURL.keys():
            self._url = self._savedURL[savedName.lower()]
        elif url != None:
            self._url = url
        else:
            raise Exception("Cannot run the discord webhook without url")
        
        self._webhook = SyncWebhook.from_url(self._url)
        

        """ Prepare logging file """
        self._logger = logging.getLogger('discord-log')
        self._logger.setLevel(logging.INFO)
        
        if not os.path.exists(self._LOG_PATH):
            os.makedirs(self._LOG_PATH)

        self._handler = RotatingFileHandler(self._LOG_PATH + '/logfile_'+self._progName+'.log', maxBytes=5242880, backupCount=5, mode="a")
        self._logger.addHandler(self._handler)
        _str_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self._logger.info('-----------------')
        self._logger.info(f'Starting %s: '%(self._progName) + _str_time)

    """
    
    Function to send message to the discord

    PARAMETER
        message  (str) : the message that will be sent
        mmention (str) : the @ mention in discord for mare specific discord notification
        log      (T/F) : change whether the log will be kept or not
    
    """
    def send(self, message, mention=None, log=True):
        prefix = ''
        if mention != None:
            if mention.lower() in ['everyone', 'all']:
                prefix = '@everyone '
            else:
                prefix = f'@%s '%(mention)
        _string = prefix + message
        self._webhook.send(_string)

        if self._prompt == 'yes':
            print('Sending to discord: ' + _string)
        if log == True:
            _str_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
            self._logger.info(_str_time + ' ' + _string)
        return

    """
    
    Fuction for testing if the module function properly or not
    
    """

    def test(self):
        self.send('Hello world!', mention='all')
        _str_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.send("The time is: "+_str_time)
        return
    
    """
    
    Function for printing arguments of the running python program
    
    """

    def send_arg(self, FLAGS):
        self.send(self._progName+' runnning with arguments: ')

        for arg in vars(FLAGS):
            _send_str = arg + ':  ' + str(getattr(FLAGS, arg))
            self.send(_send_str)
        
        return