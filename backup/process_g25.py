
import os

# List of input files to process
input_files = [
    r"d:\DonyanShare\backup\Global25_PCA_pop_averages_scaled.txt",
    r"d:\DonyanShare\backup\Global25_PCA_modern_scaled.txt"
]
output_file = r"d:\DonyanShare\Global25_PCA_pop_averages_scaled_simplified.txt"

# Translation Dictionary
TRANSLATIONS = {
    # Major Regions & Countries
    "China": "中国",
    "Taiwan": "台湾",
    "Mongolia": "蒙古",
    "Russia": "俄罗斯",
    "Japan": "日本",
    "Korea": "韩国",
    "Vietnam": "越南",
    "Thailand": "泰国",
    "Cambodia": "柬埔寨",
    "Laos": "老挝",
    "Myanmar": "缅甸",
    "India": "印度",
    "Pakistan": "巴基斯坦",
    "Iran": "伊朗",
    "Kazakhstan": "哈萨克斯坦",
    "Uzbekistan": "乌兹别克斯坦",
    "Kyrgyzstan": "吉尔吉斯斯坦",
    "Turkmenistan": "土库曼斯坦",
    "Tajikistan": "塔吉克斯坦",
    "Turkey": "土耳其",
    "Armenia": "亚美尼亚",
    "Georgia": "格鲁吉亚",
    "Azerbaijan": "阿塞拜疆",
    "Albania": "阿尔巴尼亚",
    "Greece": "希腊",
    "Italy": "意大利",
    "Spain": "西班牙",
    "France": "法国",
    "Germany": "德国",
    "UK": "英国",
    "England": "英格兰",
    "Scotland": "苏格兰",
    "Ireland": "爱尔兰",
    "Sweden": "瑞典",
    "Norway": "挪威",
    "Finland": "芬兰",
    "Estonia": "爱沙尼亚",
    "Latvia": "拉脱维亚",
    "Lithuania": "立陶宛",
    "Poland": "波兰",
    "Ukraine": "乌克兰",
    "Belarus": "白俄罗斯",
    "Romania": "罗马尼亚",
    "Bulgaria": "保加利亚",
    "Hungary": "匈牙利",
    "Czech": "捷克",
    "Slovakia": "斯洛伐克",
    "Austria": "奥地利",
    "Switzerland": "瑞士",
    "Belgium": "比利时",
    "Netherlands": "荷兰",
    "USA": "美国",
    "America": "美洲",
    "Canada": "加拿大",
    "Mexico": "墨西哥",
    "Brazil": "巴西",
    "Argentina": "阿根廷",
    "Chile": "智利",
    "Peru": "秘鲁",
    "Egypt": "埃及",
    "Morocco": "摩洛哥",
    "Algeria": "阿尔及利亚",
    "Tunisia": "突尼斯",
    "Libya": "利比亚",
    "Ethiopia": "埃塞俄比亚",
    "Kenya": "肯尼亚",
    "Nigeria": "尼日利亚",
    "SouthAfrica": "南非",
    "Australia": "澳大利亚",
    "Papua": "巴布亚",
    
    # Ethnic Groups (China & Surroundings)
    "Han": "汉族",
    "Manchu": "满族",
    "Mongol": "蒙古族",
    "Tibetan": "藏族",
    "Uyghur": "维吾尔族",
    "Hui": "回族",
    "Zhuang": "壮族",
    "Miao": "苗族",
    "Yao": "瑶族",
    "Yi": "彝族",
    "Tujia": "土家族",
    "She": "畲族",
    "Dai": "傣族",
    "Dong": "侗族",
    "Naxi": "纳西族",
    "Bai": "白族",
    "Hani": "哈尼族",
    "Lahu": "拉祜族",
    "Li": "黎族",
    "Qiang": "羌族",
    "Tu": "土族",
    "Xibe": "锡伯族",
    "Daur": "达斡尔族",
    "Oroqen": "鄂伦春族",
    "Hezhen": "赫哲族",
    "Ewenki": "鄂温克族",
    "Kazakh": "哈萨克族",
    "Kirghiz": "柯尔克孜族",
    "Tajik": "塔吉克族",
    "Uzbek": "乌兹别克族",
    "Tatar": "塔塔尔族",
    "Salar": "撒拉族",
    "Bonan": "保安族",
    "Dongxiang": "东乡族",
    "Yugur": "裕固族",
    
    # Provinces/Cities (China)
    "Beijing": "北京",
    "Shanghai": "上海",
    "Tianjin": "天津",
    "Chongqing": "重庆",
    "Heilongjiang": "黑龙江",
    "Jilin": "吉林",
    "Liaoning": "辽宁",
    "InnerMongolia": "内蒙古",
    "Hebei": "河北",
    "Shanxi": "山西",
    "Shandong": "山东",
    "Henan": "河南",
    "Shaanxi": "陕西",
    "Gansu": "甘肃",
    "Qinghai": "青海",
    "Ningxia": "宁夏",
    "Xinjiang": "新疆",
    "Anhui": "安徽",
    "Jiangsu": "江苏",
    "Zhejiang": "浙江",
    "Jiangxi": "江西",
    "Fujian": "福建",
    "Hubei": "湖北",
    "Hunan": "湖南",
    "Guangdong": "广东",
    "Guangxi": "广西",
    "Hainan": "海南",
    "Sichuan": "四川",
    "Guizhou": "贵州",
    "Yunnan": "云南",
    "Tibet": "西藏",
    "HongKong": "香港",
    "Macau": "澳门",
    
    # Time Periods & Archeological Terms
    "Paleolithic": "旧石器时代",
    "Mesolithic": "中石器时代",
    "Neolithic": "新石器时代",
    "Chalcolithic": "铜石并用时代",
    "BronzeAge": "青铜时代",
    "IronAge": "铁器时代",
    "Medieval": "中世纪",
    "Antiquity": "古典时期",
    "Historic": "历史时期",
    "Modern": "现代",
    "Ancient": "古代",
    
    # Suffixes/Prefixes (Exact matches or part of compound)
    "_BA": "_青铜时代",
    "_IA": "_铁器时代",
    "_N": "_新石器",
    "_EN": "_早期新石器",
    "_MN": "_中期新石器",
    "_LN": "_晚期新石器",
    "_EBA": "_早期青铜",
    "_MBA": "_中期青铜",
    "_LBA": "_晚期青铜",
    "_EIA": "_早期铁器",
    "_MIA": "_中期铁器",
    "_LIA": "_晚期铁器",
    "_EarlyModern": "_近代早期",
    "_Imperial": "_帝国时期",
    "_Late": "_晚期",
    "_Middle": "_中期",
    "_Early": "_早期",
    
    # Directions
    "North": "北",
    "South": "南",
    "East": "东",
    "West": "西",
    "Central": "中",
    "Northeast": "东北",
    "Northwest": "西北",
    "Southeast": "东南",
    "Southwest": "西南",
    
    # Misc
    "River": "河",
    "Basin": "盆地",
    "Plateau": "高原",
    "Island": "岛",
    "Mountain": "山",
}

def translate_name(name):
    # Split by underscore to handle parts
    parts = name.split('_')
    translated_parts = []
    
    for part in parts:
        # Check if the part exists directly in dictionary
        if part in TRANSLATIONS:
            translated_parts.append(TRANSLATIONS[part])
        else:
            # Try partial replacements if not an exact match
            temp_part = part
            # Iterate through translation dict to find partial matches
            # Sort keys by length descending to match longest substrings first
            sorted_keys = sorted(TRANSLATIONS.keys(), key=len, reverse=True)
            
            # Only replace if it looks like English (basic heuristic)
            # This is to avoid messing up things that might already be ok or unknown codes
            # But here we just assume input is English
            
            replaced = False
            for key in sorted_keys:
                if key in temp_part:
                    temp_part = temp_part.replace(key, TRANSLATIONS[key])
                    replaced = True
            
            translated_parts.append(temp_part)
            
    return "_".join(translated_parts)

def process_files():
    data_map = {}
    header = ""

    for input_file in input_files:
        print(f"Processing {input_file}...")
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Warning: File not found at {input_file}")
            continue

        # Process header
        if lines and not header:
            potential_header = lines[0]
            if potential_header.startswith(',') or 'PC1' in potential_header:
                header = potential_header
                lines = lines[1:]

        elif lines and header:
            if lines[0].startswith(',') or 'PC1' in lines[0]:
                lines = lines[1:]

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            if len(parts) < 26: 
                continue

            raw_name = parts[0]
            name_without_id = raw_name.split(':')[0]

            try:
                coords = [float(x) for x in parts[1:]]
            except ValueError:
                continue

            # Grouping logic
            name_parts = name_without_id.split('_')
            if len(name_parts) >= 2:
                group_name = f"{name_parts[0]}_{name_parts[1]}"
            else:
                group_name = name_without_id
            
            if group_name not in data_map:
                data_map[group_name] = []
            
            data_map[group_name].append(coords)

    if not data_map:
        print("No data processed.")
        return

    # Write output
    print(f"Writing output to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        if header:
            f.write(header)
        
        for group_name in sorted(data_map.keys()):
            samples = data_map[group_name]
            
            # Calculate average
            num_samples = len(samples)
            num_coords = len(samples[0])
            
            avg_coords = [0.0] * num_coords
            for sample in samples:
                for i in range(num_coords):
                    avg_coords[i] += sample[i]
            
            avg_coords = [x / num_samples for x in avg_coords]
            
            # Translate the group name
            translated_name = translate_name(group_name)
            
            # Format output line
            coords_str = ",".join([f"{x:.8f}" for x in avg_coords])
            f.write(f"{translated_name},{coords_str}\n")

    print(f"Generated {len(data_map)} grouped averages.")
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    process_files()
