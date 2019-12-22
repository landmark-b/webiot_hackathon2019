# cocnfig
import json

# For checkpoint
config = {
    "cp-id": "0001",
    "url": "http://xxx.yyy.zzz"
}

# For smartphone, raspberrypi
config_cli = {
    "appli_id": "teamE"
}

# config_json = json.dumps(config)
# print(config_json)

f = open("config.json", "w")
json.dump(config, f, ensure_ascii=False)

f_cli = open("config_cli.json", "w")
json.dump(config_cli, f_cli, ensure_ascii=False)