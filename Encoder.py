import os
from PIL import Image
class CompilerHelper:
    symbols = [
        '☺', '♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟', '♠', '♡', '♢', '♣', '♤', '♥', '♦', '♧',
        '♨', '♩', '♪', '♫', '♬', '♭', '♮', '♯', '✁', '✂', '✃', '✄', '✆', '✇', '✈', '✉', '✊', '✋', '✌', '✍', '✎',
        '✏', '✐', '✑', '✒', '✓', '✔', '✕', '✖', '✗', '✘', '✙', '✚', '✛', '✜', '✝', '✞', '✟', '✠', '✡', '✢', '✣',
        '✤', '✥', '✦', '✧', '✨', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '✱', '✲', '✳', '✴', '✵', '✶', '✷', '✸',
        '✹', '✺', '✻', '✼', '✽', '✾', '✿', '❀', '❁', '❂', '❃', '❄', '❅', '❆', '❇', '❈', '❉', '❊', '❋', '❌', '❍',
        '❎', '❏', '❐', '❑', '❒', '❓', '❔', '❕', '❖', '❗', '❘', '❙', '❚', '❛', '❜', '❝', '❞', '❟', '❠', '❡', '❢',
        '❣', '❤', '❥', '❦', '❧', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '➀', '➁', '➂', '➃', '➄', '➅',
        '➆', '➇', '➈', '➉', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '➓', '➔', '➕', '➖', '➗', '➘', '➙', '➚',
        '➛', '➜', '➝', '➞', '➟', '➠', '➡', '➢', '➣', '➤', '➥', '➦', '➧', '➨', '➩', '➪', '➫', '➬', '➭', '➮', '➯',
        '➰', '➱', '➲', '➳', '➴', '➵', '➶', '➷', '➸', '➹', '➺', '➻', '➼', '➽', '➾', '➿', '⟀', '⟁', '⟂', '⟃', '⟄',
        '⟅', '⟆', '⟇', '⟈', '⟉', '⟊', '⟋', '⟌', '⟍', '⟎', '⟏', '⟐', '⟑', '⟒', '⟓', '⟔', '⟕', '⟖', '⟗', '⟘', '⟙',
        '⟚', '⟛', '⟜', '⟝', '⟞', '⟟', '⟠', '⟡', '⟢', '⟣', '⟤', '⟥', '⟦', '⟧', '⟨', '⟩', '⟪', '⟫', '⟬', '⟭', '⟮',
        '⟯', '⟰', '⟱', '⟲', '⟳', '⟴', '⟵', '⟶', '⟷', '⟸', '⟹', '⟺', '⟻', '⟼', '⟽', '⟾', '⟿', '⤀', '⤁', '⤂', '⤃',
        '⤄', '⤅', '⤆', '⤇', '⤈', '⤉', '⤊', '⤋', '⤌', '⤍', '⤎', '⤏', '⤐', '⤑', '⤒', '⤓', '⤔', '⤕', '⤖', '⤗',
        '⤘', '⤙', '⤚', '⤛', '⤜', '⤝', '⤞', '⤟', '⤠', '⤡', '⤢', '⤣', '⤤', '⤥', '⤦', '⤧', '⤨', '⤩', '⤪', '⤫',
        '⤬', '⤭', '⤮', '⤯', '⤰', '⤱', '⤲', '⤳', '⤴', '⤵', '⤶', '⤷', '⤸', '⤹', '⤺', '⤻', '⤼', '⤽', '⤾', '⤿',
        '⥀', '⥁', '⥂', '⥃', '⥄', '⥅', '⥆', '⥇', '⥈', '⥉', '⥊', '⥋', '⥌', '⥍', '⥎', '⥏', '⥐', '⥑', '⥒', '⥓',
        '⥔', '⥕', '⥖', '⥗', '⥘', '⥙', '⥚', '⥛', '⥜', '⥝', '⥞', '⥟', '⥠', '⥡', '⥢', '⥣', '⥤', '⥥', '⥦', '⥧',
        '⥨', '⥩', '⥪', '⥫', '⥬', '⥭', '⥮', '⥯'
    ] 
    R_DELIM = '^'
    G_DELIM = '&'
    B_DELIM = '*'
    COUNT_DELIM = ']'
    @staticmethod
    def ClampColour(R: int, G: int, B: int):
        R = max(15, min(R, 240))
        G = max(15, min(G, 240))
        B = max(15, min(B, 240))
        return (R, G, B)
    @staticmethod
    def DecompressColour(Colour: str):
        try:
            R = CompilerHelper.symbols.index(Colour[0])
            G = CompilerHelper.symbols.index(Colour[1])
            B = CompilerHelper.symbols.index(Colour[2])
            return (R, G, B)
        except ValueError:
            return (0, 0, 0)
    @staticmethod
    def CompressColour(R: int, G: int, B: int):
        return CompilerHelper.symbols[R] + CompilerHelper.symbols[G] + CompilerHelper.symbols[B]
def compress_image(image_path, output_file):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    compressed_data = []
   
    for y in range(height):
        current_color = None
        run_length = 0
        row_data = []
       
        for x in range(width):
            R, G, B = CompilerHelper.ClampColour(*pixels[x, y])
            color_triplet = CompilerHelper.CompressColour(R, G, B)
           
            if color_triplet == current_color:
                run_length += 1
            else:
                if current_color is not None:
                    encoded_run = f"{run_length * 3}{CompilerHelper.COUNT_DELIM}"
                    row_data.append(f"{current_color}{encoded_run}")
                current_color = color_triplet
                run_length = 1
        if current_color is not None:
            encoded_run = f"{run_length * 3}{CompilerHelper.COUNT_DELIM}"
            row_data.append(f"{current_color}{encoded_run}")
        compressed_line = f"{y}," + "".join(row_data)
        compressed_data.append(compressed_line)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(compressed_data))
    print(f"Image compressed and saved as '{output_file}'")
def decode_and_save_image(file_path, width, height, output_image):
    with open(file_path, "r", encoding="utf-8") as file:
        compressed_lines = file.read().splitlines()
    decoded_pixels = [[(0,0,0) for _ in range(width)] for _ in range(height)]
    for line in compressed_lines:
        if ',' not in line:
            continue
        y_str, data = line.split(',', 1)
        try:
            y = int(y_str)
        except ValueError:
            continue
        if y >= height:
            continue
        x = 0
        i = 0
        while i < len(data) and x < width:
            if i + 3 > len(data):
                break
            color = data[i:i+3]
            i += 3
            count_str = ''
            while i < len(data) and data[i] != CompilerHelper.COUNT_DELIM:
                count_str += data[i]
                i += 1
            if i < len(data):
                i += 1
            if not count_str.isdigit():
                continue
            try:
                encoded_count = int(count_str)
                actual_count = encoded_count // 3
            except ValueError:
                continue
            R, G, B = CompilerHelper.DecompressColour(color)
            for _ in range(actual_count):
                if x >= width:
                    break
                decoded_pixels[y][x] = (R, G, B)
                x += 1
    flat_pixels = [pixel for row in decoded_pixels for pixel in row]
    decoded_image = Image.new("RGB", (width, height))
    decoded_image.putdata(flat_pixels)
    decoded_image.save(output_image)
    print(f"Decoded image saved as '{output_image}'")
Path = os.path.join(os.getcwd(), "Modules", "PABLO.png")
compress_image(Path, "output.txt")
i = Image.open(Path)
width, height = i.size
decode_and_save_image("output.txt", width, height, "decoded_image.png")
