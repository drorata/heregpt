import typer
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from heregpt.models import TaskBase
from heregpt import utils

app = typer.Typer()

load_dotenv(override=False)

console = Console()


@app.command()
def main(tool: str, task: str):
    task = TaskBase(tool=tool, task=task)
    task.build_prompt()
    console.print("About to send the following prompt🚀", style="#5f5fff")
    print(task.prompt)
    console.print("End of prompt", style="#5f5fff")
    abort = typer.confirm("Abort?", default=True)
    if abort:
        print("Aborting!")
        raise typer.Exit(10)

    response = utils.get_completion(task.prompt)
    console.print(response)
