# my_band.py
from band import Band
from musician import Musician
from guitar import Guitar


def main():
    # Create a band
    band = Band("Extreme")

    # Create musicians and add guitars
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))

    # Add musicians to the band
    band.add(nuno)
    band.add(Musician("Gary Cherone"))  # No instruments added

    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)

    kevin = Musician("Kevin Figueiredo")  # No instruments added
    band.add(kevin)

    # Print the band information
    print("band (str)")
    print(band)

    # Print what each band member is playing or not playing
    print("band.play()")
    print(band.play())


if __name__ == "__main__":
    main()
