import requests
from time import sleep
from rich.console import Console
from datetime import datetime
import json

console = Console()

URL = "https://example-cyndi.000webhostapp.com/grading.php"

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
