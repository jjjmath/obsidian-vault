import os
import re

def fix_format_in_file(file_path):
    """修复文件格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割成行
    lines = content.split('\n')
    new_lines = []
    in_frontmatter = False
    modified = False
    
    for i, line in enumerate(lines):
        # 检测到frontmatter开始
        if line.strip() == '---' and i == 0:
            in_frontmatter = True
            new_lines.append(line)
            continue
        
        # 检测到frontmatter结束
        if line.strip() == '---' and in_frontmatter and i > 0:
            in_frontmatter = False
            new_lines.append(line)
            continue
        
        # 在frontmatter区域内，修复格式
        if in_frontmatter:
            # 修复 title:xxx 为 title: xxx
            if re.match(r'^title:\S', line):
                new_line = re.sub(r'^(title:)(\S)', r'\1 \2', line)
                new_lines.append(new_line)
                modified = True
                continue
            # 修复 作者:xxx 为 作者: xxx
            if re.match(r'^作者:\S', line):
                new_line = re.sub(r'^(作者:)(\S)', r'\1 \2', line)
                new_lines.append(new_line)
                modified = True
                continue
            # 修复 日期:xxx 为 日期: xxx
            if re.match(r'^日期:\S', line):
                new_line = re.sub(r'^(日期:)(\S)', r'\1 \2', line)
                new_lines.append(new_line)
                modified = True
                continue
            # 修复 版权:xxx 为 版权: xxx
            if re.match(r'^版权:\S', line):
                new_line = re.sub(r'^(版权:)(\S)', r'\1 \2', line)
                new_lines.append(new_line)
                modified = True
                continue
        
        new_lines.append(line)
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        return True
    
    return False

def main():
    base_path = r'd:\高中数学math\obsidian-vault\Projects'
    fixed_count = 0
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    if fix_format_in_file(file_path):
                        print(f'Fixed: {file}')
                        fixed_count += 1
                except Exception as e:
                    print(f'Error processing {file}: {e}')
    
    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main()
