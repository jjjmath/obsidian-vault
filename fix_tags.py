import os
import re

def fix_tags_in_file(file_path):
    """修复文件中的tags格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有tags部分
    if 'tags:' not in content:
        return False
    
    # 分割成行
    lines = content.split('\n')
    new_lines = []
    in_tags = False
    modified = False
    
    for line in lines:
        # 检测到tags:行
        if line.strip() == 'tags:':
            in_tags = True
            new_lines.append(line)
            continue
        
        # 在tags区域内，且行以空格开头，包含 - -
        if in_tags and re.match(r'^(\s+)-\s+-', line):
            # 替换 - - 为 -
            new_line = re.sub(r'^(\s+)-\s+-', r'\1- ', line)
            new_lines.append(new_line)
            modified = True
            continue
        
        # 检测到tags区域结束（新的属性或---）
        if in_tags and (line.strip() and not line.startswith(' ') and not line.startswith('\t')):
            in_tags = False
        
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
                    if fix_tags_in_file(file_path):
                        print(f'Fixed: {file}')
                        fixed_count += 1
                except Exception as e:
                    print(f'Error processing {file}: {e}')
    
    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main()
