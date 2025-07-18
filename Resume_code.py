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
plt.subplots_adjust(top=0.96, bottom=0.04,left=0.06,right=0.94)



#underlining
underline_locations = [
    [.049,.218,.13],
    [0.8285,0.1605,.8675]
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


def writeSkillTree(main_skill_name,attrs,loc,skill_color='#000000', attr_color='#000000',bullet=0,base_font_size=10,offset_font_size1=2,offset_font_size2=3,std_weight='regular'):
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
            plt.annotate(attr,loc, weight=std_weight, fontsize=base_font_size-offset_font_size1, color=attr_color )
        loc = offset(loc,x=-.0225)
    return loc

def JobDescription(jobTitle,company="",DateRange="",loc=[],tasks=[""],general_desciption="",skills_used=[],base_font_size=13,offset_font_size1=3,offset_font_size2=4,default_task_spacing_height=0.025,default_skill_spacing_height=0.025):
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
plt.axhline(y=0.84, xmin=.715, xmax=1.1,  color=BLACK, alpha=0.1, linewidth=1 )
plt.axhline(y=0.24, xmin=.715, xmax=1,  color=BLACK, alpha=0.1, linewidth=1 )


plt.annotate('<<Coded And Generated in Python by,', (0.02,0.98), weight=STANDARD_WEIGHT, fontsize=8, alpha=0.75 )
plt.annotate(PERSON, (0.02,0.94), weight=BOLD, fontsize=14, color='#222222')
plt.annotate('Developer    Engineer', (0.02,0.91), weight=STANDARD_WEIGHT, fontsize=14, color='#222222' )
plt.annotate('&', (0.131,0.91), weight=STANDARD_WEIGHT, fontsize=14, color='#aa00ff' )

xValues = [.1665,.1765,.1865,.2165]
for i in range(4):
    if i==0:continue
    plt.axhline(y=0.957 - i*.007, xmin=xValues[i], xmax=.67,  color='#000000', alpha=0.09 - .02*(i-1), linewidth=1 )


arr_code = mpimg.imread(PHONE_ICON)
imagebox1 = OffsetImage(arr_code, zoom=.8)
ab1 = AnnotationBbox(imagebox1, (0.735, 1.2),frameon=False)
ax.add_artist(ab1)
plt.annotate(f'      Cell:  {CONTACT_CELL}', (0.75,1.2), weight=BOLD, fontsize=9, color='#222222')



##Contact Information
    
#cell
arr_code = mpimg.imread(PHONE_ICON)
imagebox = OffsetImage(arr_code, zoom=.8)
ab = AnnotationBbox(imagebox, (0.735, 0.98),frameon=False)
ax.add_artist(ab)
plt.annotate(f'      Cell:  {CONTACT_CELL}', (0.75,0.97), weight=BOLD, fontsize=9, color='#222222')

#email

arr_code = mpimg.imread(EMAIL_ICON)
imagebox = OffsetImage(arr_code, zoom=0.375)
ab = AnnotationBbox(imagebox, (0.735, 0.93),frameon=False)
ax.add_artist(ab)
plt.annotate(f'      Email:  {CONTACT_EMAIL}', (0.75,0.920), weight=BOLD, fontsize=9, color='#222222')

#Location

arr_code = mpimg.imread(LOCATION_ICON)
imagebox = OffsetImage(arr_code, zoom=0.055)
ab = AnnotationBbox(imagebox, (0.735, 0.885),frameon=False)
ax.add_artist(ab)
plt.annotate('       Location:  Chicago, IL', (0.75,0.87), weight=BOLD, fontsize=9, color='#222222')

plt.annotate('GitHub', (0.82,0.165), weight=BOLD, fontsize=9.5, color="#646464AB")
plt.annotate('https://github.com/aaronsighs/Resume', (0.72,0.14), weight=BOLD, fontsize=8.5, color="#22222286")


# skill section
loc=writeSkillTree("Python",[{"Openpyxl & Pandas & Numpy":["Excel/Data Automation"]},{"Pyqt/Tkinter":["Graphics User Interface"]}],(0.70,.81),skill_color="#7722ff")
loc=writeSkillTree("Web",[{"Databases":["Mongodb","SQL"]},{"Front-End":["Html/Css/Javascript/React"]},"Rest-Apis"],(0.70,loc[1]-.035),skill_color="#7722ff")
loc=writeSkillTree("Excel",
                   [{"VBA":["UI",'Automation','Data Analaysis']}
                    ,"Well Versed with Formulas","Pivot-Tables"],(0.70,loc[1]-.035),skill_color="#7722ff")
loc=writeSkillTree("Software Development",
                   [{"Scripting":["Autohotkey",'debugging']}
                  ],(0.70,loc[1]-.035),skill_color="#7722ff")



#Job2
JobDescription("Sales Engineer",loc=[.035,.82],company="Carl Stahl Decorcable",DateRange="May 2024 - Present",
               general_desciption="Sales Engineer for a Manufacturing Company",
               tasks=[
                      "+ Generate proposals for large goverment, residential and commercial projects across the U.S",
                      "+ Developed sales tool using python to analyze bid proposals and design systems for customers",
                      "+ Create Excel tools to standardize raw, shorthand measurement data, eliminating errors and ",
                       "providing consistent data for production.",
                      "+ Collaborate closely with clients to understand their techincal requirments and providing unique solutions",
                      "+ Examine existing team workflows, identify areas of inefficiency, and implement improved standardization",
                      "practices",
                      "+ Leverage Excel to improve proposal submissions and accuracy"],
                skills_used=[])

#Job1
JobDescription("Sales Engineer",loc=[.035,.53],company="Takisawa Lathes",DateRange="August 2021 - May 2024",
               general_desciption="Sales engineer/leadership role for a small lathe mfg. company",
               tasks=[
                      "+ Managed relationships with up to 80 clients across the United States",
                      "+ Provided timely support and insight into products and features",
                      "+ Reviewed Cad drawings for high-Valued clients to determine optimum production times",
                      "+ Developed Excel forms and and quoting tools to support sales and technical divisions",
                      "+ Worked on the Social Media Team to plan and promote products",
                      "+ Created Optical Charachter Readers ( OCR ) in Python to process large paperwork"],
                skills_used=[])

#schooling
JobDescription("BSE Degree",loc=[.035,.28],company="SIUE University",DateRange="Grad. 2020",
               general_desciption="Bachelors of Science in Electrical Engineering",
               tasks=["+ Senior Design: Designed and developed a fish tank monitoring and feeding system:",
                      "consisting of a website and onboard user inteface which read sensors to monitor "," aquarium health and activated a motor to feed fish.",
                      "+ Worked with large sets of radar data in matlab to predict weather conditions",
                      "+ Worked on the robotics team to help with guidance and navigation system using python"
                      ])


#output

#plt.savefig("resume.png")
plt.savefig("resume.pdf")

plt.show()

