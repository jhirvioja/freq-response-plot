import typer
import pandas as pd
import matplotlib.pyplot as plt

app = typer.Typer()


@app.command()
def main(
    input_file: str = typer.Argument(..., help="Path to the input CSV file"),
    name: str = typer.Option(
        "frequency_response", help="Base name for output files and plot title"
    ),
    ylim: tuple[float, float] = typer.Option(
        None, help="Fixed y-axis limits as (min, max)"
    ),
):
    """
    Load frequency response data from a CSV file, plot it, and save both the plot and a cleaned CSV.
    """
    df = pd.read_csv(input_file, comment="#", skipinitialspace=True)

    typer.echo(df.info())
    typer.echo(df.head())

    plt.figure(figsize=(12, 6))
    plt.plot(df["frequency"], df["raw"])
    plt.xscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.title(name)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Response (dB)")
    plt.xlim(20, 20000)
    if ylim:
        plt.ylim(ylim)
    plt.xticks(
        [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000],
        labels=["20", "50", "100", "200", "500", "1k", "2k", "5k", "10k", "20k"],
    )
    plt.tight_layout()

    plot_filename = f"{name}.png"
    csv_filename = f"clean_{name}.csv"

    plt.savefig(plot_filename)
    df.to_csv(csv_filename, index=False)

    typer.echo(f"✅ Plot saved to {plot_filename}")
    typer.echo(f"✅ CSV saved to {csv_filename}")


if __name__ == "__main__":
    app()
