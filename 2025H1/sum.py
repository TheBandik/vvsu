import sys

def process_md_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    table_start = None
    table_end = None
    
    for i, line in enumerate(lines):
        if '|' in line:
            if table_start is None:
                table_start = i
            table_end = i
    
    if table_start is None or table_end is None:
        print("Таблица не найдена.")
        return
    
    table_lines = [line.strip() for line in lines[table_start:table_end + 1]]
    header, separator, *rows = table_lines
    headers = [cell.strip() for cell in header.split('|')[1:-1]]
    
    lab_indexes = [i for i, h in enumerate(headers) if h.startswith("Лаб")]
    attendance_index = headers.index("Посещаемость") if "Посещаемость" in headers else None
    ir_index = headers.index("ИР") if "ИР" in headers else None
    at1_index = headers.index("АТ1") if "АТ1" in headers else None
    at1_grade_index = headers.index("Оценка") if "Оценка" in headers else None
    at2_index = headers.index("АТ2") if "АТ2" in headers else None
    at2_grade_index = headers.index("Оценка", at1_grade_index + 1) if at1_grade_index is not None else None
    final_score_index = headers.index("Итоговые баллы") if "Итоговые баллы" in headers else None
    final_grade_index = headers.index("Итоговая оценка") if "Итоговая оценка" in headers else None
    
    def get_grade(score, thresholds):
        for threshold, grade in thresholds:
            if score <= threshold:
                return grade
        return thresholds[-1][1]
    
    at1_thresholds = [(23, "2"), (29, "3"), (35, "4"), (40, "5")]
    at2_thresholds = [(36, "2"), (45, "3"), (54, "4"), (60, "5")]
    final_thresholds = [(61, "2"), (75, "3"), (90, "4"), (float('inf'), "5")]
    
    new_rows = []
    
    for row in rows:
        cells = [cell.strip() for cell in row.split('|')[1:-1]]
        
        try:
            # Для АТ1 суммируем все ячейки до столбца АТ1, исключая "№" и "Оценка"
            at1 = sum(float(cells[i]) for i in range(at1_index) if cells[i].replace('.', '', 1).isdigit() and headers[i] not in ["№", "Оценка"])
        except ValueError:
            at1 = 0
        
        try:
            # Для АТ2 суммируем все ячейки до столбца АТ2, исключая "№", "Оценка" и уже учтенное значение АТ1
            at2 = sum(float(cells[i]) for i in range(at2_index) if cells[i].replace('.', '', 1).isdigit() and headers[i] not in ["№", "Оценка"]) - at1 * 2
        except ValueError:
            at2 = 0
        
        # Итоговые баллы = АТ1 + АТ2
        final_score = at1 + at2
        
        # Обновляем значения в таблице
        if at1_index is not None:
            cells[at1_index] = str(int(at1)) if at1.is_integer() else str(at1)
        if at1_grade_index is not None:
            cells[at1_grade_index] = get_grade(at1, at1_thresholds)
        if at2_index is not None:
            cells[at2_index] = str(int(at2)) if at2.is_integer() else str(at2)
        if at2_grade_index is not None:
            cells[at2_grade_index] = get_grade(at2, at2_thresholds)
        if final_score_index is not None:
            cells[final_score_index] = str(int(final_score)) if final_score.is_integer() else str(final_score)
        if final_grade_index is not None:
            cells[final_grade_index] = get_grade(final_score, final_thresholds)
        
        new_rows.append('| ' + ' | '.join(cells) + ' |')
    
    updated_table = '\n'.join([header, separator] + new_rows) + '\n'
    lines[table_start:table_end + 1] = [updated_table]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <путь к файлу>")
    else:
        process_md_table(sys.argv[1])
