
def calculate_jiaodong_average():
    # Data from the selected lines
    data = [
        "辽宁大连LiuYi,0.020488,-0.453942,0.001131,-0.061047,0.05201,0.008367,-0.007285,0.005077,-0.008999,0.002734,-0.079895,-0.009891,0.00892,-0.002752,-0.002172,-0.00769,-0.001304,-0.002914,-0.006034,-0.003252,0.016845,0.001237,0.017748,0.002771,0.005628",
        "山东潍坊团,0.025041,-0.450895,0.007542,-0.063954,0.050471,0.021753,0.013396,0.003923,-0.014521,0.004374,-0.08022,-0.007194,0.006541,-0.007019,-0.009908,0.001193,0.005867,0.001014,-0.005028,-0.004002,0.011729,0.006677,0.007272,-0.000964,-0.007185",
        "PEEN,0.017073,-0.443786,0.010182,-0.062016,0.050779,0.025937,0.002115,0.001154,-0.021066,-0.001822,-0.064631,-0.016186,0.013528,-0.009771,-0.015201,-0.008353,-0.001304,-0.008235,-0.00352,-0.016508,0.012852,0.004575,0.005669,0.00494,-0.003832"
    ]

    all_coords = []
    for line in data:
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
    
    # Format: keep 8 decimal places like previous entries
    coords_str = ",".join([f"{x:.8f}" for x in avg_coords])
    result_line = f"胶东,{coords_str}"
    
    print(result_line)
    
    # Append to file
    with open(r"d:\DonyanShare\单个样本.txt", 'a', encoding='utf-8') as f:
        f.write(result_line + "\n")

if __name__ == "__main__":
    calculate_jiaodong_average()
