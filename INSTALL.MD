## Currently this documentation is incomplete
## Be aware of what you are doing

At first, git clone this repository here with:  
```
git clone https://github.com/Chill-Engine/ChillZone-Server chillserver
```  
Or download it from ``Code > Download ZIP``
Then, open server folder and install all requirements with command:
```
cd chillserver
pip install -r requirements.txt
```
After installation, run server with:
```
flask run
```
When server will be closed, change these parameters in configs folder:
    ***serverConfig.json***
 - ``servername`` - Your server name;  
 - ``app_id`` - Application ID from Discord Developers page
 - ``admin`` - Admin Name (Will be removed in future (when i'll make panel))
 - ``bpic`` - List of pictures for large section from Rich Presence > Art Assets
 - ``spic`` - Same as bpic but for small section
    ***panelConfig.json***
    (Change them before second launch( because of encryption ))
 - ``adminUsername`` - Your username for admin panel 
 - ``adminPassword`` - Your password for admin panel