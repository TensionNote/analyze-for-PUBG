from PIL import Image,ImageDraw
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
    # draw = Image.new('RGB', (600, 250), (128, 128, 128))
    for landing_point in landing_point_list:
        draw = ImageDraw.Draw(map_img)
        x=int(landing_point[0]*0.01)
        y=int(landing_point[1]*0.01)
        draw.point(((x, y)), fill=(255, 255, 0))
    return map_img