class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print("✅ Authentification réussie.")
        else:
            print("❌ Nom d'utilisateur ou mot de passe incorrect.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("🚫 Veuillez vous authentifier.")
        if amount <= 0:
            raise Exception("🚫 Le montant doit être positif.")
        self.balance += amount
        print(f"💰 Dépôt de {amount}€ effectué. Nouveau solde : {self.balance}€")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("🚫 Veuillez vous authentifier.")
        if amount <= 0:
            raise Exception("🚫 Le montant doit être positif.")
        if amount > self.balance:
            raise Exception("🚫 Fonds insuffisants.")
        self.balance -= amount
        print(f"🏧 Retrait de {amount}€ effectué. Nouveau solde : {self.balance}€")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("🚫 Veuillez vous authentifier.")
        if amount <= 0:
            raise Exception("🚫 Le montant doit être positif.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("🚫 Retrait refusé : minimum balance non respecté.")
        self.balance -= amount
        print(f"🏧 Retrait de {amount}€ effectué. Nouveau solde : {self.balance}€")


class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("🚫 account_list doit contenir uniquement des comptes valides.")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("⚠️ try_limit invalide. Défini à 2 par défaut.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Se connecter")
            print("2. Quitter")
            choix = input("Choisissez une option : ")
            if choix == "1":
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
                self.log_in(username, password)
            elif choix == "2":
                print("👋 Merci d'avoir utilisé le distributeur.")
                break
            else:
                print("❌ Choix invalide.")

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print(f"❌ Tentative {self.current_tries}/{self.try_limit}")
        if self.current_tries >= self.try_limit:
            print("🚫 Trop de tentatives. Fermeture du programme.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n=== MENU COMPTE ===")
            print("1. Déposer")
            print("2. Retirer")
            print("3. Quitter le compte")
            choix = input("Choisissez une option : ")
            if choix == "1":
                try:
                    montant = int(input("Montant à déposer : "))
                    account.deposit(montant)
                except Exception as e:
                    print(e)
            elif choix == "2":
                try:
                    montant = int(input("Montant à retirer : "))
                    account.withdraw(montant)
                except Exception as e:
                    print(e)
            elif choix == "3":
                print("👋 Déconnexion.")
                break
            else:
                print("❌ Choix invalide.")
if __name__ == "__main__":
    acc1 = BankAccount("mohamed", "pass123", 100)
    acc2 = MinimumBalanceAccount("amina", "secret", 200, minimum_balance=50)

    atm = ATM([acc1, acc2], try_limit=3)

