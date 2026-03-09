
def calculate_manchu_average():
    # Original data
    all_data = [
        "满族,0.02528500,-0.44625243,0.01034393,-0.06374636,0.04715157,0.02091679,0.00602621,0.00311529,-0.01234443,0.00304586,-0.07134657,-0.00786821,0.00792150,-0.00723493,-0.00687329,0.00046400,-0.00241193,0.00013571,-0.00318736,-0.00606543,0.01057957,0.00360364,0.01006221,0.00036150,-0.00216407",
        "满族_Jinzhou,0.02055938,-0.44353237,0.01105438,-0.06379250,0.04691250,0.02042869,0.00534644,0.00356225,-0.01096750,0.00414594,-0.07109556,-0.00711881,0.00975594,-0.00388800,-0.00625156,-0.00087850,-0.00132012,0.00167856,-0.00247481,-0.01011431,0.00924925,0.00597400,0.00924369,0.00007537,0.00036675",
        "满族_辽宁,0.02249199,-0.44796478,0.00878369,-0.06489272,0.04963095,0.02056521,0.00497175,0.00217296,-0.01167283,0.00467738,-0.07449741,-0.00833010,0.01079027,-0.00610986,-0.00808389,-0.00063118,0.00058405,0.00067173,-0.00419646,-0.01018584,0.01121200,0.00763041,0.01097675,0.00028742,0.00086071"
    ]

    # Target lines to remove
    target_names = ["满族", "满族_Jinzhou", "满族_辽宁"]

    all_coords = []
    for line in all_data:
        parts = line.split(',')
        coords = [float(x) for x in parts[1:]]
        all_coords.append(coords)

    num_samples = len(all_coords)
    num_coords = len(all_coords[0])
    avg_coords = [0.0] * num_coords

    for coords in all_coords:
        for i in range(num_coords):
            avg_coords[i] += coords[i]

    avg_coords = [x / num_samples for x in avg_coords]
    
    # Format: keep 8 decimal places
    coords_str = ",".join([f"{x:.8f}" for x in avg_coords])
    result_line = f"满族,{coords_str}"
    
    print(f"Result: {result_line}")
    
    # Read existing file content
    file_path = r"d:\DonyanShare\标杆样本库.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    # Filter out old lines and prepare new content
    new_lines = []
    manchu_added = False
    
    for line in lines:
        name = line.split(',')[0].strip()
        if name in target_names:
            # Skip this line
            continue
        else:
            new_lines.append(line)
            
    # Find a good place to insert or just append
    # Since we are replacing multiple lines, we can append to the end or insert where the first one was.
    # But for simplicity and safety, let's append to the end if not found, or maybe insert at the position of the first removed line.
    
    # Let's try to insert at the position of the first removed line to keep some order
    first_index = -1
    for i, line in enumerate(lines):
        name = line.split(',')[0].strip()
        if name in target_names:
            first_index = i
            break
    
    if first_index != -1:
        # We need to adjust index because we filtered the list `new_lines`
        # It's tricky to map indices. 
        # Simpler approach: Iterate again, when hitting the first target, add the new line, then skip all targets.
        
        final_lines = []
        added = False
        for line in lines:
            name = line.split(',')[0].strip()
            if name in target_names:
                if not added:
                    final_lines.append(result_line + "\n")
                    added = True
                # Skip the old line
            else:
                final_lines.append(line)
        new_lines = final_lines
    else:
        new_lines.append(result_line + "\n")

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("File updated successfully.")

if __name__ == "__main__":
    calculate_manchu_average()
