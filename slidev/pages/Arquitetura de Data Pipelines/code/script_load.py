

def load(df, name_file):
    
    df.write.csv(name_file, header=True, mode="overwrite")
    print("Arquivo salvo com sucesso!")