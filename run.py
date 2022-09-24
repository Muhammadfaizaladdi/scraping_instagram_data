import datetime
from src.yaml_loader import yaml_loader
from src.get_post import get_instagram_posts
from src.json_to_pd import parse_instafiles
import os
import pandas as pd

# Download variabel konfigurasi yang dibutuhkan 
insta_vars = yaml_loader("variables.yaml")

# Nama akun dan password yang akan digunakan untuk login
USER = insta_vars["user"]
PASSWORD = insta_vars["pswd"]

# Daftar nama akun yang akan di load datanya
list_of_users = insta_vars["username"]

# Range tanggal untuk pengambilan data
startdate = datetime.datetime(2021,1,1)
enddate = datetime.datetime(2022,8,1)

# Default Path
initial_path = insta_vars["initial_path"]

def run():
  # Mendownload data dari setiap user, dimana datanya akan di simpan secara default di folder data pada path folder saat ini
  for user in list_of_users:
    get_instagram_posts(USER, PASSWORD, user, startdate, enddate, initial_path, save_folder="data")

  # Load data dalam bentuk json menjadi dataframe
  list_df_of_users = []
  for user in list_of_users:
    df_instagram = parse_instafiles(user, os.getcwd(), initial_path)
    list_df_of_users.append(df_instagram)

  # Menggabungkan semua data frame dari setiap users
  full_data = pd.concat(list_df_of_users)

  # Save the data dalam bentuk excel
  full_data.to_excel("data/selebgram_gorontalo.xlsx", index=False)


if __name__ == "__main__":
  run()