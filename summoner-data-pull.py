import requests
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

RIOT_API_ENDPOINT = 'https://na1.api.riotgames.com/lol'
API_KEY = ''

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter your summoner name:")
        self.label.pack(side="left")

        self.summoner_name_entry = tk.Entry(self)
        self.summoner_name_entry.pack(side="left")

        self.button = tk.Button(self, text="Get data", command=self.get_data)
        self.button.pack(side="left")

        self.summoner_info_label = tk.Label(self, text='')
        self.summoner_info_label.pack()

    def get_data(self):
        summoner_name = self.summoner_name_entry.get()
        response = requests.get(f'{RIOT_API_ENDPOINT}/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}')

        if response.status_code == 200:
            summoner_data = response.json()

            self.summoner_info_label.config(text=f"Summoner ID: {summoner_data['id']}")
            self.account_id_label = tk.Label(self, text=f"Account ID: {summoner_data['accountId']}")
            self.account_id_label.pack()
            self.puuid_label = tk.Label(self, text=f"PUUID: {summoner_data['puuid']}")
            self.puuid_label.pack()
            self.name_label = tk.Label(self, text=f"Name: {summoner_data['name']}")
            self.name_label.pack()
            self.summoner_level_label = tk.Label(self, text=f"Level: {summoner_data['summonerLevel']}")
            self.summoner_level_label.pack()
        else:
            print(f'Error {response.status_code}: {response.content}')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
