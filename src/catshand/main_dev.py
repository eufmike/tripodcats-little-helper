import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def prjinit(
    rootdir: Annotated[
        str,
        typer.Option("--root_dir", "-d", help="directory for the project folder"),
    ],
    prj_n: Annotated[
        str,
        typer.Option("--project_name", "-n", help="project name (example: EP028)"),
    ],
    mat_dir: Annotated[
        str,
        typer.Option("--material_dir", "-m", help="directory for the material folder"),
    ],
):
    """prjinit creates the project folder"""
    import catshand.tools as tools

    tools.prjinit.main(
        rootdir=rootdir,
        prj_n=prj_n,
        mat_dir=mat_dir,
    )


@app.command()
def test(name: str):
    print(name)


if __name__ == "__main__":
    app()
