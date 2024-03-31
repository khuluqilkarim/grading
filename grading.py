import requests
import urllib.request
from time import sleep
from rich.console import Console
from datetime import datetime
import json
import pandas as pd
import sys

VERSI = "v1.4"

if len(sys.argv) != 2:
    print("Usage: python grading [argumen]\n-> \033[32mstart\033[0m\tstart grading\n-> \033[32mscore\033[0m\tLeader board\n-> \033[32mupdate\033[0m\tupdate grading tool")
    sys.exit(1)

arg = sys.argv[1]
URL = "https://example-cyndi.000webhostapp.com/grading.php"
URLSCORE = "https://example-cyndi.000webhostapp.com/score.php"



console = Console()

if arg == "start":
    soal = input(f"\033[94m[{datetime.now().strftime('%H:%M:%S')}]\033[0m Enter The Question Code : ")

    params_1 = {
        'soal': soal,
    }
    response = requests.get(URL, params=params_1)
    if response.text == "1":
        console.log("question code exist")
        nama = input(f"\033[94m[{datetime.now().strftime('%H:%M:%S')}]\033[0m Name: ")
        jawaban = input(f"\033[94m[{datetime.now().strftime('%H:%M:%S')}]\033[0m Answer: ")

        params_2 = {
            'nama': nama,
            'soal': soal,
            'jawaban': jawaban
        }

        params_3 = {
            'nama': nama,
        }
    

        response = requests.get(URL, params=params_2)
        response_score = requests.get(URL,params_3)
        response_obj = json.loads(response_score.text)
        total_score = response_obj['total_score']
        if response.text == "1":
            tasks = ["Validating Connection","Question Code","Submitted Task"]
            with console.status("[bold green]Working on tasks...") as status:
                while tasks:
                    task = tasks.pop(0)
                    sleep(1)
                    console.log(f"[bold green]✔[/bold green] {task} [bold green]complete[/bold green]")
            console.log(f"\nYour Score : {total_score}")
        elif response.text == "0":
            tasks = ["Validating Connection","Wrong Answer","Submitted Task"]
            with console.status("[bold green]Working on tasks...") as status:
                while tasks:
                    task = tasks.pop(0)
                    sleep(1)
                    console.log(f"[bold red]✘[/bold red] {task} [bold red]Error[/bold red]") 
        else:
            print("Error")

        
    else:
        tasks = ["Validating Connection","Enter question code does not exist","question code does not exist"]
        with console.status("[bold green]Working on tasks...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(1)
                console.log(f"[bold red]✘[/bold red] {task} [bold red]Error[/bold red]") 
elif arg == "score":
    response = requests.get(URLSCORE)
    if response.status_code == 200:
        tasks = ["Validating Connection","Status code 200","Printing Score"]
        with console.status("[bold green]Working on tasks...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(1)
                console.log(f"[bold green]✔[/bold green] {task} [bold green]complete[/bold green]")
        console.log("\n[bold green]Leader Board[bold green]\n")
        data_json = response.text
        data = json.loads(data_json)

        df = pd.DataFrame(data)
        print(df)
elif arg == "update":
    UPDATE = "https://example-cyndi.000webhostapp.com/update/update.php"

    response_update = requests.get(UPDATE)
    response_obj = json.loads(response_update.text)

    versi_tools = response_obj[0]['versi']  

    if versi_tools > VERSI:
        url = 'https://raw.githubusercontent.com/khuluqilkarim/grading/master/grading.py'
        file_name = 'grading.py'
        urllib.request.urlretrieve(url, file_name)
        console.log("You are on the latest version now")
        sys.exit(1)
    else:
        console.log("You are on the latest version")
        
