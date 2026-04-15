#!/bin/bash
# Git推送脚本 - 解决认证问题

REPO_PATH="/mnt/e/obsidian-vault/obsidian-vault"

echo "🚀 开始Git同步流程..."
echo "======================="

cd "$REPO_PATH" || exit 1

# 1. 检查当前状态
echo "1. 当前Git状态:"
git status --short

# 2. 检查远程仓库
echo -e "\n2. 远程仓库配置:"
git remote -v

# 3. 设置HTTPS方式
echo -e "\n3. 设置HTTPS远程URL:"
git remote set-url origin https://github.com/jjjmath/obsidian-vault.git
echo "   ✅ 已设置为HTTPS"

# 4. 配置Git凭据缓存（15分钟）
echo -e "\n4. 配置Git凭据缓存:"
git config --global credential.helper 'cache --timeout=900'
echo "   ✅ 凭据缓存已设置（15分钟）"

# 5. 尝试推送（可能需要输入凭据）
echo -e "\n5. 开始推送更新..."
echo "   ========================================="
echo "   如果提示输入凭据："
echo "   - Username: jjjmath"
echo "   - Password: 你的GitHub个人访问令牌"
echo "   ========================================="

# 设置环境变量避免交互问题
export GIT_TERMINAL_PROMPT=1
export GIT_ASKPASS=/bin/echo

# 尝试推送
git push origin main 2>&1 | tee /tmp/git_push.log

if [ $? -eq 0 ]; then
    echo -e "\n🎉 推送成功！"
    echo "======================="
    echo "已同步内容："
    echo "- 更新了SCHEMA.md（高中数学教学定位）"
    echo "- 优化了index.md（按高中数学模块组织）"
    echo "- 创建了高考数学、数学课程标准实体页面"
    echo "- 生成了完整报告文档"
else
    echo -e "\n⚠️  推送失败，请手动操作："
    echo "======================="
    echo "手动步骤："
    echo "1. 登录GitHub创建个人访问令牌"
    echo "2. 运行：git push origin main"
    echo "3. 输入用户名：jjjmath"
    echo "4. 输入密码：你的个人访问令牌"
fi