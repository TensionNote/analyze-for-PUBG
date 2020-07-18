from PIL import Image,ImageDraw,ImageFont
def load_map(map_name):
    # Baltic_Main, Desert_Main, DihorOtok_Main, Erangel_Main, Range_Main, Savage_Main, Summerland_Main 
    path_map={
        "Miramar":"./map/Miramar_Main_High_Res.png",
        "Erangel":"./map/Erangel_Remastered_Main_High_Res.png"
    }
    img = Image.open(path_map[map_name])
    img = img.convert("RGB")
    return img

def resize_map(img):
    img = img.resize((5000, 5000))
    return img

def draw_landing_point(map_img, landing_point_list):
    color_map={
        "1":"fuchsia",
        "2":"Lime",
        "3":"Blue",
        "4":"maroon",
        "5":"olive",
        "6":"red",
        "7":"green",
        "8":"navy",
        "9":"yellow",
        "10":"aqua",
        "11":"gray",
        "12":"purple",
        "13":"teal",
        "14":"silver",
        "15":"black",
        "16":"orangered"
    }
    draw = ImageDraw.Draw(map_img)
    for landing_point in landing_point_list:
        x=int(landing_point[0]*0.01)
        y=int(landing_point[1]*0.01)
        draw.ellipse((x-30,y-30,x+30,y+30), outline=(0, 0, 0), fill=color_map[str(landing_point[4])])
        # draw.text(xy, text, fill=None, font=None)
        font = ImageFont.truetype("./font/Myriad Pro Bold SemiExtended.ttf", 40)
        draw.text((x+40,y-40), landing_point[3], fill="black",font=font)
    return map_img