import tkinter as tk

root = tk.Tk()
root.title("Exemple de formulaire")
root.geometry("600x400")

# Ajouter les champs de saisie et les labels
label1 = tk.Label(root, text="Nom:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Adresse:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Ajouter le bouton
button = tk.Button(root, text="Valider")
button.pack()

# Lancer la boucle principale de l'application
root.mainloop()