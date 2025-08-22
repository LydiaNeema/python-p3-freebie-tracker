#!/usr/bin/env python3

# Script goes here!
from models import Company,Dev,Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

company1 = Company(name= "Google",founding_year = 1998)
company2 = Company(name= "Amazon",founding_year = 1994)
company3 = Company(name= "Microsoft",founding_year = 1975)

dev1 = Dev(name ="Lydia")
dev2 = Dev(name ="Bob")
dev3 = Dev(name= "Alice")

freebie1 = Freebie(item_name="Sticker",value=5,company=company1,dev=dev1)
freebie2 = Freebie(item_name="Mug",value=10,company=company2,dev=dev2)
freebie3 = Freebie(item_name="T-Shirt",value=20,company=company3,dev=dev3)

session.add_all([company1,company2,company3,dev1,dev2,dev3,freebie1,freebie2,freebie3])
session.commit()
session.close()


