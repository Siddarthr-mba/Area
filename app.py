
import streamlit as st
import numpy as np
import sys,os
from src.shapes import *

#Add the path to the src directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def GetUserInputs():
    drop_down_col, _= st.columns(2)

    with drop_down_col:
        ShapeName=st.selectbox("Select Shape",["Circle","Rectangle"],index=0)

    if ShapeName == "Circle":
        Radius=st.number_input("Radius in cm (integer)", value=0, step=1)
        shape=Circle(Radius)
        area=shape.getArea()
        st.write(f"Area of Circle is {area}")
        
        #args:list[int]=[Radius]
        # shape:Shape= globals()[ShapeName]()
        # AreaOfCircle=Shape.Circle.get(Radius)
        # st.write(f"Area of Circle :blue {AreaOfCircle}]")
    else:
        Length=st.number_input("Length in cm (integer)", value=0, step=1)
        Breadth=st.number_input("Breadth in cm (integer)", value=0, step=1)
        shape = Rectangle(Length, Breadth)
        area = shape.getArea()
        st.write(f"Area of Rectangle is {area}")
       
             
        #args:list[int] = [Length,Breadth]
        # AreaOfRectangle=Shape.Rectangle(Length,Breadth)
        # st.write(f"Area of Circle :blue {AreaOfRectangle}]")
    #shape:Shape= globals()[ShapeName](*args)
    #st.write("Area of " +ShapeName+" is "+str(shape.getArea()))
 #   GetArea()

#def GetArea():
#    CalculateArea=st.button("GetArea")
       
if __name__=="__main__":
    st.set_page_config(page_title="APP TO CALCULATE AREA", 
                       page_icon=None, 
                       layout="centered")
    GetUserInputs()