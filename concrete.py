# (c) 2025 Cheska Piquero and Joshuamae Gongob
# C. Material Strength Calculation for Steel

def main():
    Length = float(input("What is the Length of the sidewalk (m)?"))
    Width = float(input("What is the Width of the sidewalk (m)?"))
    Depth = float(input("What is the Depth of the sidewalk (m)?"))
    
    Volume = Length * Width * Depth
    
    print(f"\So, you need (Volume:,.2f) cubic meters of concrete.")

if __name__ == "__main__":
 main()