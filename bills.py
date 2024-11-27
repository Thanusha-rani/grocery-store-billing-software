from tkinter import*
import random,os;
from tkinter import messagebox
import mysql.connector


mydb = mysql.connector.connect(
  user="12345",
  password="password",
  database="my_db"
)

#CLASS
class Bill_App:
	def __init__ (self,root):
		self.root=root
		
		#Window Screen dimensions 
		self.root.geometry("1350x770+0+0")
		#Window title 
		self.root.title("Grocery Store Billing Software")
		bg_color="#1d1f21"

		
		#TITLE
		#bd-border ; relief-border style; fg-foreground color; pack - fill
		title=Label(self.root,text="The Dark Store - Invoice Manager",bd=12,relief=GROOVE,bg=bg_color,fg="white", font=("times new roman",30,"bold"),pady=2).pack(fill=X)


		#Customer details Variable
		self.customer_name=StringVar();
		self.customer_ph=StringVar();
		self.customer_BillNo=StringVar();
		x=random.randint(1000,9999);
		self.customer_BillNo.set(str(x));
		self.search_bill=StringVar();


		#Cosmetics Details Variable
		self.soap=IntVar();
		self.faceCream=IntVar();
		self.faceWash=IntVar();
		self.HairSpray=IntVar();
		self.HairGel=IntVar();


		#Grocery Details Variable
		self.Rice=IntVar()
		self.FoodOil=IntVar()
		self.Daal=IntVar()
		self.Wheat=IntVar()
		self.Sugar=IntVar()



		#ColdDrinks details Variable
		self.Pepsi=IntVar()
		self.Mirinda=IntVar()
		self.Sting=IntVar()
		self.LemonMalt=IntVar()
		self.Sprite=IntVar()


		#Billing Menu Variable
		self.totalCosmeticsPrice=StringVar();
		self.totalGroceryPrice=StringVar();
		self.totalDrinksPrice=StringVar();


		#Taxes Variable
		self.CosmeticsTax=StringVar();
		self.GroceryTax=StringVar();
		self.ColdDrinksTax=StringVar();

		#Total Bill
		self.totalBill=StringVar();

		#flag
		self.flag=0;

		#Payment Option
		self.v=StringVar();


		#=================================================Customer=============================================================

		F1=LabelFrame(self.root,bg=bg_color,text="Enter Customer Details",font=("times new roman",15,"bold"),fg="gold")
		F1.place(x=0,y=80,relwidth=1)

		cust_name_lbl=Label(F1,text="Customer Name :",bg=bg_color,fg="white", font=("times new roman,10",10,"bold")).grid(row=0,column=0,padx=20,pady=5);
		cust_text_entry=Entry(F1,width="18",textvariable=self.customer_name, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5);


		cust_phone_lbl=Label(F1,text="Phone No. :",bg=bg_color,fg="white",font=("times new roman,10",10,"bold")).grid(row=0,column=5,padx=20,pady=5);
		cust_phone_entry=Entry(F1,width="18",textvariable=self.customer_ph,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=8,padx=10,pady=5);


		cust_bill_lbl=Label(F1,text="Bill Number" ,bg=bg_color,fg="white", font=("times new roman,10",10,"bold")).grid(row=0,column=10,padx=20,pady=5);
		cust_bill_entry=Entry(F1,width="20",textvariable=self.customer_BillNo,font="arial 15 ", bd=7,relief=SUNKEN).grid(row=0,column=12,padx=10,pady=5);


		btn_bill=Button(F1,text="Search",command=self.find_bill,width=18,bd=10).grid(row=0,column=15)


		#=================================================Cosmetic Detail=============================================================


		F2=LabelFrame(self.root,bd=10,relief=GROOVE, bg=bg_color,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold");
		F2.place(x=5,y=170,width=325,height=380)


		CosmeticsP1=Label(F2,text="Bath Soap",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=30,pady=15)
		CosmeticsP1_Entry=Entry(F2,width="15",textvariable=self.soap,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=30,pady=15);


		CosmeticsP2=Label(F2,text="Face Cream",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=30,pady=15)
		CosmeticsP2_Entry=Entry(F2,width="15",textvariable=self.faceCream,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=5,padx=30,pady=15);


		CosmeticsP3=Label(F2,text="Face Wash",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=30,pady=15)
		CosmeticsP3_Entry=Entry(F2,width="15",textvariable=self.faceWash,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=5,padx=30,pady=15);



		CosmeticsP4=Label(F2,text="Hair spray",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=30,pady=15)
		CosmeticsP4_Entry=Entry(F2,width="15",textvariable=self.HairSpray,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=5,padx=30,pady=15);



		CosmeticsP5=Label(F2,text="Hair Gel",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=4,column=0,padx=30,pady=15)
		CosmeticsP5_Entry=Entry(F2,width="15",textvariable=self.HairGel,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=4,column=5,padx=30,pady=15);



		#=================================================Grocery Detail=============================================================



		F3=LabelFrame(self.root,bd=10,relief=GROOVE, bg=bg_color,text="Grocery",font=("times new roman",15,"bold"),fg="gold");
		F3.place(x=330,y=170,width=325,height=380)




		GroceryP1=Label(F3,text="Rice",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=30,pady=15)
		GroceryP1_Entry=Entry(F3,width="15",textvariable=self.Rice,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=30,pady=15);





		GroceryP2=Label(F3,text="Food oil",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=30,pady=15)
		GroceryP2_Entry=Entry(F3,width="15",textvariable=self.FoodOil,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=5,padx=30,pady=15);



		GroceryP3=Label(F3,text="Daal",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=30,pady=15)
		GroceryP3_Entry=Entry(F3,width="15",textvariable=self.Daal,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=5,padx=30,pady=15);



		GroceryP4=Label(F3,text="Wheat",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=30,pady=15)
		GroceryP4_Entry=Entry(F3,width="15",textvariable=self.Wheat,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=5,padx=30,pady=15);



		GroceryP5=Label(F3,text="Sugar",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=4,column=0,padx=30,pady=15)
		GroceryP5_Entry=Entry(F3,width="15",textvariable=self.Sugar,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=4,column=5,padx=30,pady=15);


		#=================================================Cold Drink Detail=============================================================



		F4=LabelFrame(self.root,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE);
		F4.place(x=655,y=170,width=325,height=380)	


		ColdDrinkP1=Label(F4,text="Pepsi",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=30,pady=15)
		ColdDrinkP1_Entry=Entry(F4,width="15",textvariable=self.Pepsi,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=30,pady=15);





		ColdDrinkP2=Label(F4,text="Mirinda",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=30,pady=15)
		ColdDrinkP2_Entry=Entry(F4,width="15",textvariable=self.Mirinda,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=5,padx=30,pady=15);



		ColdDrinkP3=Label(F4,text="Sting",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=30,pady=15)
		ColdDrinkP3_Entry=Entry(F4,width="15",textvariable=self.Sting,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=5,padx=30,pady=15);



		ColdDrinkP4=Label(F4,text="Lemon Malt",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=30,pady=15)
		ColdDrinkP4_Entry=Entry(F4,width="15",textvariable=self.LemonMalt,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=5,padx=30,pady=15);



		ColdDrinkP5=Label(F4,text="Sprite",bg=bg_color,fg="#5cb484",font=("times new roman",12,"bold")).grid(row=4,column=0,padx=30,pady=15)
		ColdDrinkP5_Entry=Entry(F4,width="15" ,textvariable=self.Sprite,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=4,column=5,padx=30,pady=15);



	#==========================================Bill Display Area===========================================


		Bill_f=Frame(self.root, bd=10,relief=GROOVE);
		Bill_f.place(x=1000,y=170,width=350,height=380);


		Bil_Label=Label(Bill_f,text=" INVOICE ",bd=3,relief=GROOVE, font=("Comic Sans MS",14,"bold")).pack(fill=X)

		scroll_y=Scrollbar(Bill_f,orient=VERTICAL)

		self.txtarea=Text(Bill_f,yscrollcommand=scroll_y.set)

		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_y.config(command=self.txtarea.yview)

		self.txtarea.pack(fill = BOTH,expand=1)


		#=================================================Total Summary Amount Detail=============================================================



		F5=LabelFrame(self.root,text="Billing Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE);
		F5.place(x=5,y=550,relwidth=1,height=150);
		
		totalCosmeticsPrice=Label(F5,text="Total Cosmetic Price",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=0,column=0,padx=2,pady=0);
		totalCosmetics_Entry=Entry(F5,width="20",textvariable=self.totalCosmeticsPrice ,font="arial 8",bd=8,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=0)

		totalGroceryPrice=Label(F5,text="Total Grocery Price",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=1,column=0,padx=2,pady=0);
		totalGrocery_Entry=Entry(F5,width="20",textvariable=self.totalGroceryPrice ,font="arial 8",bd=8,relief=SUNKEN).grid(row=1,column=5,padx=5,pady=00)

		totalColdDrinksPrice=Label(F5,text="Total Cold Drinks Price",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=2,column=0,padx=2,pady=0);
		totalColdDrinks_Entry=Entry(F5,width="20",textvariable=self.totalDrinksPrice ,font="arial 8",bd=8,relief=SUNKEN).grid(row=2,column=5,padx=5,pady=0)


		#=================================================Tax Detail=============================================================



		totalCosmeticsTax=Label(F5,text="Cosmetic GST",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=0,column=20,padx=2,pady=0);
		totalCosmetics_Entry=Entry(F5,width="20",textvariable=self.CosmeticsTax ,font="arial 8",bd=8,relief=SUNKEN).grid(row=0,column=30,padx=5,pady=0)

		totalGroceryTax=Label(F5,text="Grocery GST",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=1,column=20,padx=2,pady=0);
		totalGrocery_Entry=Entry(F5,width="20",textvariable=self.GroceryTax ,font="arial 8",bd=8,relief=SUNKEN).grid(row=1,column=30,padx=5,pady=00)

		totalColdDeinksTax=Label(F5,text="Cold Drinks GST",fg="white",font=("times new roman",15,"bold"),bg=bg_color).grid(row=2,column=20,padx=2,pady=0);
		totalColdDrinks_Entry=Entry(F5,width="20",textvariable=self.ColdDrinksTax ,font="arial 8",bd=8,relief=SUNKEN).grid(row=2,column=30,padx=5,pady=0)
	

		#=================================================Different Buttoons =============================================================


		btn_F=Frame(F5,bd=7,relief=GROOVE);
		btn_F.place(x=700,y=2,width=600,height=100);


		total_btn=Button(btn_F,command=self.total,text="Total",width=10,height=2,bd=5,bg="#32c412",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,pady="10",padx="5")
		generate_Bill_btn=Button(btn_F,command=self.bill_area,text="Generate Bill",width=10,height=2,bd=5,bg="#124ac4",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=3,pady="10",padx="5")
		clear_btn=Button(btn_F,text="Clear All",command=self.clear_btn,width=10,height=2,bd=5,bg="#c45312",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=6,pady="10",padx="5")
		Exit_btn=Button(btn_F,text="Exit",command=self.exit_btn,width=10,height=2,bd=5,bg="#de2a30",fg="white",font=("times new roman",15,"bold")).grid(row=0,column=9,pady="10",padx="5")

		#=================================================Payment Detail=============================================================
		
		F6=LabelFrame(self.root,text="Payment Options",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE);
		F6.place(x=5,y=700,relwidth=1,height=70);
		
		self.v.set(1)
		l = [("Cash", "Cash"),("Credit Card","Credit Card"),("Debit Card","Debit Card"),("UPI/Paytm","UPI/Paytm")]
		for l,val in l:
			Radiobutton(F6,text=l,padx=5,variable=self.v,value=val,relief=GROOVE,font=("times new roman",15,"bold"),bg="white").pack(side="left")

		self.welcome_bill()


	def total(self):
		self.flag=1;

		#Cosmetics Products Price

		self.soapPrice=40;
		self.faceCreamPrice=100;
		self.faceWashPrice=120;
		self.HairSprayPrice=180;
		self.HairGelPrice=220;


		#Grocery Products Price

		self.RicePrice=100;
		self.FoodOilPrice=300;
		self.DaalPrice=60;
		self.WheatPrice=70;
		self.SugarPrice=110;

		#Cold Drinks Price

		self.PepsiPrice=30
		self.MirindaPrice=30
		self.LemonMaltPrice=60
		self.StingPrice=40
		self.SpritePrice=25


		#Categories Tax
		self.CosmeticCategoryTax=0.12;
		self.GroceryCategoryTax=0.07;
		self.ColdDrinkCategoryTax=0.05;




		self.totalCosmeticsPriceCalculated=float(		
											(self.soap.get()*self.soapPrice)+
											(self.faceCream.get()*self.faceCreamPrice)+
											(self.faceWash.get()*self.faceWashPrice)+
											(self.HairSpray.get()*self.HairSprayPrice)+
											(self.HairGel.get()*self.HairGelPrice)
											)
												
		self.totalCosmeticsPrice.set("Rs."+str(self.totalCosmeticsPriceCalculated));
		self.CosmeticsTax.set("Rs."+str(round((self.totalCosmeticsPriceCalculated*self.CosmeticCategoryTax),2)));



		self.totalGroceryPriceCalculated=float(		
											(self.Rice.get())*self.RicePrice+
											(self.FoodOil.get()*self.FoodOilPrice)+
											(self.Daal.get()*self.DaalPrice)+
											(self.Wheat.get()*self.WheatPrice)+
											(self.Sugar.get()*self.SugarPrice)
											)
												
		self.totalGroceryPrice.set("Rs."+str(self.totalGroceryPriceCalculated));

		self.GroceryTax.set("Rs."+str(round((self.totalGroceryPriceCalculated*self.GroceryCategoryTax),2)));



		self.totalColdDrinksPriceCalculated=float(		
											(self.Pepsi.get())*self.PepsiPrice+
											(self.Mirinda.get()*self.MirindaPrice)+
											(self.Sting.get()*self.StingPrice)+
											(self.LemonMalt.get()*self.LemonMaltPrice)+
											(self.Sprite.get()*self.SpritePrice)
											)
												
		self.totalDrinksPrice.set("Rs."+str(self.totalColdDrinksPriceCalculated));
		self.ColdDrinksTax.set("Rs."+str(round((self.totalColdDrinksPriceCalculated*self.ColdDrinkCategoryTax),2)));



		self.totalBill.set((self.totalCosmeticsPriceCalculated+self.totalGroceryPriceCalculated+self.totalColdDrinksPriceCalculated)+
			(self.totalCosmeticsPriceCalculated*self.CosmeticCategoryTax)+
			(self.totalGroceryPriceCalculated*self.GroceryCategoryTax)+
			(self.totalColdDrinksPriceCalculated*self.ColdDrinkCategoryTax));

	def welcome_bill(self):
		self.txtarea.delete("1.0",END);
		self.txtarea.insert(END,"\tWelcome to The Dark Store"); 
		self.txtarea.insert(END,f"\nBill Number : {self.customer_BillNo.get()}");
		self.txtarea.insert(END,f"\nCustomer Name : {self.customer_name.get()}");
		self.txtarea.insert(END,f"\nPhone Number : {self.customer_ph.get()}");

		self.txtarea.insert(END,f"\n======================================");
		self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice");
		self.txtarea.insert(END,f"\n======================================");


	def bill_area(self):


		if self.customer_name.get()=="" or self.customer_ph.get()=="":
			messagebox.showerror("Error","Customer Details must");
		elif self.flag==0:
			messagebox.showerror("Error","First Calculate Total Bill");

		elif self.totalCosmeticsPrice.get()=="Rs.0.0"and self.totalGroceryPrice.get()=="Rs.0.0" and self.totalDrinksPrice.get()=="Rs.0.0":
			messagebox.showerror("Error","you are not purchase anything");
		else:
			self.welcome_bill();
			if self.soap.get()>0:
				self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.soapPrice*self.soap.get()}");


			if self.faceCream.get()>0:
				self.txtarea.insert(END,f"\nFace Cream\t\t{self.faceCream.get()}\t\t{self.faceCreamPrice*self.faceCream.get()}");

			if self.faceWash.get()>0:
				self.txtarea.insert(END,f"\nFace Wash\t\t{self.faceWash.get()}\t\t{self.faceWashPrice*self.faceWash.get()}");

			if self.HairSpray.get()>0:
				self.txtarea.insert(END,f"\nHair Spray\t\t{self.HairSpray.get()}\t\t{self.HairSprayPrice*self.HairSpray.get()}");

			if self.HairGel.get()>0:
				self.txtarea.insert(END,f"\nHair Gel\t\t{self.HairGel.get()}\t\t{self.HairGelPrice*self.HairGel.get()}");

			if self.Rice.get()>0:
				self.txtarea.insert(END,f"\nRice\t\t{self.Rice.get()}\t\t{self.RicePrice*self.Rice.get()}");

			if self.FoodOil.get()>0:
				self.txtarea.insert(END,f"\nFood Oil\t\t{self.FoodOil.get()}\t\t{self.FoodOilPrice*self.FoodOil.get()}");

			if self.Daal.get()>0:
				self.txtarea.insert(END,f"\nDaal\t\t{self.Daal.get()}\t\t{self.DaalPrice*self.Daal.get()}");

			if self.Wheat.get()>0:
				self.txtarea.insert(END,f"\nWheat\t\t{self.Wheat.get()}\t\t{self.WheatPrice*self.Wheat.get()}");

			if self.Sugar.get()>0:
				self.txtarea.insert(END,f"\nSugar\t\t{self.Sugar.get()}\t\t{self.SugarPrice*self.Sugar.get()}");

			if self.Pepsi.get()>0:
				self.txtarea.insert(END,f"\nPepsi\t\t{self.Pepsi.get()}\t\t{self.PepsiPrice*self.Pepsi.get()}");

			if self.Mirinda.get()>0:
				self.txtarea.insert(END,f"\nMirinda\t\t{self.Mirinda.get()}\t\t{self.MirindaPrice*self.Mirinda.get()}");

			if self.Sting.get()>0:
				self.txtarea.insert(END,f"\nSting\t\t{self.Sting.get()}\t\t{self.StingPrice*self.Sting.get()}");

			if self.LemonMalt.get()>0:
				self.txtarea.insert(END,f"\nLemon Malt\t\t{self.LemonMalt.get()}\t\t{self.LemonMaltPrice*self.LemonMalt.get()}");

			if self.Sprite.get()>0:
				self.txtarea.insert(END,f"\nSprite\t\t{self.Sprite.get()}\t\t{self.SpritePrice*self.Sprite.get()}");



			self.txtarea.insert(END,f"\n--------------------------------------");

			if(self.CosmeticsTax.get()!="Rs.0.0"):
				self.txtarea.insert(END,f"\nCosmetic Tax : \t\t\t{self.CosmeticsTax.get()}");

			if(self.GroceryTax.get()!="Rs.0.0"):
				self.txtarea.insert(END,f"\nGrocery Tax : \t\t\t{self.GroceryTax.get()}");

			if(self.ColdDrinksTax.get()!="Rs.0.0"):
				self.txtarea.insert(END,f"\nCold Drink Tax : \t\t\t{self.ColdDrinksTax.get()}");


			self.txtarea.insert(END,f"\nTotal Bill : \t\t\tRs.{self.totalBill.get()}");
			self.txtarea.insert(END,f"\n--------------------------------------");
			self.txtarea.insert(END,f"\n--------------------------------------");
			self.txtarea.insert(END,f"\nPayment Method : \t\t\t-{self.v.get()}");
			self.txtarea.insert(END,f"\n--------------------------------------");
			self.txtarea.insert(END,f"\nThanks For Shopping with us");
			self.txtarea.insert(END,f"\nPlease Visit Again");
			self.save_bill();


	def save_bill(self):
		response=messagebox.askyesno("Saved","Do you want to save this bill");
		if(response>0):
			self.bill_data=self.txtarea.get("1.0",END); 
			f1=open("bills/"+str(self.customer_BillNo.get())+".txt","w");
			f1.write(self.bill_data);
			f1.close();
			mycursor = mydb.cursor()
			sql = "INSERT INTO bill (name, bill_no,total_bill) VALUES (%s, %s, %s)"
			val = (self.customer_name.get(), self.customer_BillNo.get(),self.totalBill.get())
			mycursor.execute(sql, val)
			mydb.commit()

			messagebox.showinfo("Saved",f"Bill no {self.customer_BillNo.get()} saved succesfully");
		else:
			return
		

	def clear_btn(self):
		response=messagebox.askyesno("Clear","Do you really want to clear?");

		if(response>0):
				#Customer details Variable
			self.customer_name.set("");
			self.customer_ph.set("");
			self.customer_BillNo.set("");
			x=random.randint(1000,9999);
			self.customer_BillNo.set(str(x));
			self.search_bill=StringVar();


			#Cosmetics Details Variable
			self.soap.set(0);
			self.faceCream.set(0);
			self.faceWash.set(0);
			self.HairSpray.set(0);
			self.HairGel.set(0);


			#Grocery Details Variable
			self.Rice.set(0);
			self.FoodOil.set(0);
			self.Daal.set(0);
			self.Wheat.set(0);
			self.Sugar.set(0);



			#ColdDrinks details Variable
			self.Pepsi.set(0);
			self.Mirinda.set(0);
			self.Sting.set(0);
			self.LemonMalt.set(0);
			self.Sprite.set(0);


			#Billing Menu Variable
			self.totalCosmeticsPrice.set("");
			self.totalGroceryPrice.set("");
			self.totalDrinksPrice.set("");


			#Taxes Variable
			self.CosmeticsTax.set("");
			self.GroceryTax.set("");
			self.ColdDrinksTax.set("");

			#Total Bill
			self.totalBill.set("");
		else:
			return;

	def exit_btn(self):
		response=messagebox.askyesno("Exit","Do you really want to Exit");
		if response>0:
			self.root.destroy();
		else:
			return;

	def find_bill(self):
		for i in os.listdir("bills/"):
			if i.split('.')[0]==self.customer_BillNo.get():
				self.txtarea.delete("1.0",END);
				f1=open(f"bills/{i}","r");
				for d in f1:
					self.txtarea.insert(END,d);
				f1.close();
				return;
			
		messagebox.showerror("Error","Invalid Bill");




root=Tk()

obj=Bill_App(root)

root.mainloop();
