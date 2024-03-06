#imports
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage,AnnotationBbox
import matplotlib.image as mpimg


##General Setup 


#Constants

PERSON = "Aaron Syers"
CONTACT_CELL = "815-666-4316"
CONTACT_EMAIL = "aaronsyers@gmail.com"

BLACK = '#000000'
BOLD = 'bold'
STANDARD_WEIGHT = "regular"

#Icons by Icon8
EMAIL_ICON = "icons8-email-64.png"
PHONE_ICON = "icons8-cell-30.png"
LOCATION_ICON = "buildings.png"


# Font Choice
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

#Page size and color
fig,ax = plt.subplots(figsize = (8.5,11))
ax.set_facecolor('white')
plt.axis('off')



#underlining
underline_locations = [
    [.05,.398,.16]
]
for location in underline_locations:
    plt.axhline(y=location[1], xmin=location[0], xmax=location[2],  color=BLACK,alpha=1, linewidth=.5 )


##General Functions
def copyShallow(arr):
    newArray = []
    for val in arr:
        newArray.append(val)
    return newArray

def offset(loc,x=0,y=0,inPlace=0):
    if inPlace:
        loc =  [loc[0]+x,loc[1]+y]
        return loc
    temp = copyShallow(loc)
    return [temp[0]+x,temp[1]+y]


def writeSkillTree(main_skill_name,attrs,loc,skill_color='#000000', attr_color='#000000',bullet=0,base_font_size=11,offset_font_size1=3,offset_font_size2=4,std_weight='regular'):
    if bullet:
        plt.annotate('[]',loc, weight=std_weight, fontsize=base_font_size, color=skill_color )
    loc = offset(loc,x=.0225)
    plt.annotate(main_skill_name.title(),loc, weight=std_weight, fontsize=base_font_size, color=skill_color )
    for attr in attrs:
        loc = offset(loc,y=-.0225)
        plt.annotate(">",loc, weight=std_weight, fontsize=base_font_size-offset_font_size1, color=attr_color )
        loc = offset(loc,x=.0225)
        if not isinstance(attr,type('')):
            name = list(attr.keys())[0]
            plt.annotate(name,loc, weight=std_weight, fontsize=base_font_size-offset_font_size1, color=attr_color )
            for value in attr[name]:
                
                loc = offset(loc,y=-.0225)
                plt.annotate("-",loc, weight=std_weight, fontsize=base_font_size-offset_font_size2, color=attr_color )
                loc = offset(loc,x=.0225)
                plt.annotate(value,loc, weight=std_weight, fontsize=base_font_size-offset_font_size2, color=attr_color )
                loc = offset(loc,x=-.0225)
        else:
            plt.annotate(attr,loc, weight=std_weight, fontsize=10, color=attr_color )
        loc = offset(loc,x=-.0225)
    return loc

def JobDescription(jobTitle,company="",DateRange="",loc=[],tasks=[""],general_desciption="",skills_used=[],base_font_size=11,offset_font_size1=3,offset_font_size2=4,default_task_spacing_height=0.025,default_skill_spacing_height=0.025):
    if not len(loc): return
    og_loc = [loc[0],loc[1]]
    plt.annotate(jobTitle,loc, weight='bold', fontsize=base_font_size-1)
    plt.annotate(company,offset(loc,x=.2225), fontsize=base_font_size-2.5, )
    plt.annotate(DateRange,offset(loc,x=.4725), fontsize=base_font_size-4.5, )
    loc = offset(loc,y=-.025)
    plt.annotate(general_desciption,offset(loc,x=.1), fontsize=base_font_size-3.5, )
    loc = offset(loc,y=-.010,x=.025)
    for text in tasks:
        
        loc = offset(loc,y=-default_task_spacing_height,)
        if text[0::-1]!="+":
            loc[0] = og_loc[0] + .02

        else:
            loc[0] = og_loc[0]

        plt.annotate(text,loc, fontsize=base_font_size-5.5, )
    loc = offset(loc,y=-.025,)
    loc[0] = og_loc[0]+.075
    for skill in skills_used:
        plt.annotate(skill,loc, fontsize=base_font_size-4.75, )
        loc = offset(loc,x=.18)
        if loc[0]>=.5:
            loc = offset(loc,y=-default_skill_spacing_height)
            loc[0] = og_loc[0]+.075







ax.axvline(x=0.7, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=5 )
plt.axvline(x=0.7, color=BLACK, alpha=0.1, linewidth=1 )
plt.axhline(y=0.84, xmin=.715, xmax=1,  color=BLACK, alpha=0.1, linewidth=1 )
plt.axhline(y=0.34, xmin=.715, xmax=1,  color=BLACK, alpha=0.1, linewidth=1 )


plt.annotate('<<Coded And Generated in Python by,', (0.02,0.98), weight=STANDARD_WEIGHT, fontsize=8, alpha=0.75 )
plt.annotate(PERSON, (0.02,0.94), weight=BOLD, fontsize=14, color='#222222')
plt.annotate('Developer    Engineer', (0.02,0.91), weight=STANDARD_WEIGHT, fontsize=14, color='#222222' )
plt.annotate('&', (0.146,0.91), weight=STANDARD_WEIGHT, fontsize=14, color='#aa00ff' )

xValues = [.0365,.0365,.1265,.2165]
for i in range(4):
    if i==0:continue
    plt.axhline(y=0.957 - i*.007, xmin=xValues[i], xmax=.67,  color='#000000', alpha=0.09 - .02*i, linewidth=1 )



##Contact Information
    
#cell
arr_code = mpimg.imread(PHONE_ICON)
imagebox = OffsetImage(arr_code, zoom=0.65)
ab = AnnotationBbox(imagebox, (0.73, 0.98),frameon=False)
ax.add_artist(ab)
plt.annotate(f'Cell:  {CONTACT_CELL}', (0.75,0.975), weight=BOLD, fontsize=9, color='#222222')

#email

arr_code = mpimg.imread(EMAIL_ICON)
imagebox = OffsetImage(arr_code, zoom=0.25)
ab = AnnotationBbox(imagebox, (0.73, 0.93),frameon=False)
ax.add_artist(ab)
plt.annotate(f'Email:  {CONTACT_CELL}', (0.75,0.925), weight=BOLD, fontsize=9, color='#222222')

#Location

arr_code = mpimg.imread(LOCATION_ICON)
imagebox = OffsetImage(arr_code, zoom=0.04)
ab = AnnotationBbox(imagebox, (0.73, 0.89),frameon=False)
ax.add_artist(ab)
plt.annotate(' Location:  Chicago,IL', (0.75,0.885), weight=BOLD, fontsize=9, color='#222222')


# skill section
loc=writeSkillTree("Python",[{"Openpyxl & Pandas & Numpy":["Excel/Data Automation"]},{"Pyqt/Tkinter":["Graphics User Interface"]},"Problem Solving"],(0.70,.81),skill_color="#7722ff")
loc=writeSkillTree("Web",[{"Databases":["Mongodb","SQL"]},{"Front-End":["Html/Css/Javascript/React"]},"Rest-Apis"],(0.70,loc[1]-.035),skill_color="#7722ff")
loc=writeSkillTree("Excel",
                   [{"VBA":["UI",'Automation','Data Analaysis']}
                    ,"High-Productivty"
                    ,"Well Versed with Formulas"],(0.70,loc[1]-.035),skill_color="#7722ff")



#Job1
JobDescription("Sales Engineer",loc=[.035,.81],company="Takisawa Lathes",DateRange="August 2021 - Present",
               general_desciption="Sales engineer/leadership role for a small lathe mfg. company",
               tasks=[
                      "+ Manage Relationships with up to 80 clients across the United States.",
                      "+ Provide Timely Support and Insight into Products and Features",
                      "+ Review Cad Drawings for High-Valued clients to determine optimum production times",
                      "+ Develop Excel forms and and quoting tools to support sales and technical divisions",
                      "+ Worked on the Social Media Team to plan and promote products",
                      "+ Created Optical Charachter Readers ( OCR ) in Python to process large paperwork"],

               skills_used = ["Project-Managment","Team-Collaboration","Customer-Relations","Problem-Solving","Adaptability","Technical Expertise","CRM",""])

#schooling
JobDescription("BSE Degree",loc=[.035,.46],company="SIUE University",DateRange="Grad. 2020",
               general_desciption="Bachelors of Science in Electrical Engineering",
               tasks=["+ Senior Design: Designed and developed a fish tank monitoring and feeding system:",
                      "consisting of a website and onboard user inteface which read sensors to monitor "," aquarium health and activated a motor to feed fish.",
                      "+ Worked with large sets of radar data in matlab to predict weather conditions",
                      "+ Worked on the robotics team to help with guidance and navigation system using python"
                      ])


#additonal skills
JobDescription("Additional Skills",loc=[.035,.25],company="",DateRange="",
               general_desciption="",
               tasks=[],

               skills_used = ["Windows/Mac/Linux","Presentation Skills","Java","Git","Computer Science","TypeScript","C++","Bash + PowerShell","Pivot Tables"])
    
plt.savefig("resume.png")
plt.show()

