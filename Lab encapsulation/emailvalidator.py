class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def validate(self, email):
        if '@' not in email or '.' not in email.split('@')[1]:
            return False
        
        name, rest = email.split('@')
        mail, domain = rest.split('.')

        if len(name) >= self.__min_length:
            if mail in self.__mails:
                if domain in self.__domains:
                    return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))      
print(email_validator.validate("georgios@gmail.net"))    
print(email_validator.validate("stamatito@abv.net"))     
print(email_validator.validate("abv@softuni.bg"))        

