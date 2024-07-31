class House:
    def __init__(self, flatno: int = None, bhk: int = None, sqrft: int = None, mail: str = None, block: int = None, wing: int = None, owner: str = None, phnno: int = None, id: str = None, pwd: str = None,status:str=None):
        self.__UName = id
        self.__pwd = pwd
        self.__FlatNo = flatno
        self.__bhk = bhk
        self.__sqrft = sqrft
        self.__mail = mail
        self.__Block = block
        self.__Owner = owner
        self.__ContactDetails = phnno
        self.__Wing = wing
        self.__status=status
    
    def get_owner(self):
        return self.__Owner
    
    def get_status(self):
        return self.__status
    
    def get_contact_details(self):
        return self.__ContactDetails
    
    def get_flat_no(self):
        return self.__FlatNo
    
    def get_bhk(self):
        return self.__bhk
    
    def get_square_feet(self):
        return self.__sqrft
    
    def get_email(self):
        return self.__mail
    
    def get_block(self):
        return self.__Block
    
    def get_wing(self):
        return self.__Wing
    
    def get_username(self):
        return self.__UName
    
    def get_password(self):
        return self.__pwd

    def get_all_details(self):
        return {
            "Owner": self.__Owner,
            "ContactDetails": self.__ContactDetails,
            "FlatNo": self.__FlatNo,
            "BHK": self.__bhk,
            "SquareFeet": self.__sqrft,
            "Email": self.__mail,
            "Block": self.__Block,
            "Wing": self.__Wing,
            "status":self.__status
        }
    def set_owner(self, owner: str):
        self.__Owner = owner
    
    def set_status(self, status: str):
        self.__status = status
    
    def set_contact_details(self, contact_details: int):
        self.__ContactDetails = contact_details
    
    def set_flat_no(self, flat_no: int):
        self.__FlatNo = flat_no
    
    def set_bhk(self, bhk: int):
        self.__bhk = bhk
    
    def set_square_feet(self, square_feet: int):
        self.__sqrft = square_feet
    
    def set_email(self, email: str):
        self.__mail = email
    
    def set_block(self, block: int):
        self.__Block = block
    
    def set_wing(self, wing: int):
        self.__Wing = wing

    def get_user_details(self):
        return {
            "Owner": self.__Owner,
            "ContactDetails": self.__ContactDetails,
            "FlatNo": self.__FlatNo,
            "Block": self.__Block,
            "Wing": self.__Wing,
            "BHK": self.__bhk,
            "SquareFeet": self.__sqrft
        }
