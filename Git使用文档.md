# Git使用文档

<u>说明,如果命令不会用的去学习linux教程</u> 

git的中文官方网址:    https://git-scm.com/book/en/v2

#### 安装完成配置

1.git config --global user.name "此处填写Github上面的名字" 设置登陆名字,引号不可省略

2.git config --global user.email "xxx@xxxx.xxx" 设置登陆邮箱

#### 获取 Git 仓库

使用$ git init 初始化一个本地仓库..

克隆现有的仓库

git clone 后面跟上github上面的上面地址,例如($ git clone https://github.com/libgit2/libgit2)

在本地仓库操作 (要先进入克隆下来的目录..例如 cd python   上传到github上去必须在python文件夹里面进行)

#### 记录每次更新到仓库

git status    											    --检查当前文件状态
git add                   									 工作区添加到暂存区域
git commit -m "说明,github上显示"	   将暂存区域添加到本地仓库
git push                        			 				 将本地同步到远程  



git 删除github上的文件
硬盘删除文件后，执行$ git status


会提示你仍然需要$ git rm <文件>

此时如果是要删除大批量文件，这么一个一个命令下去不得累死人啊

其实可以这样（不管之前有没有已经本地物理删除）

执行 $ git rm * -r（记得，cd 到你要删除的目录下。当然 * 可以换成指定目录）

这时删除文件已经进入本地缓存区，

接下来就是正常的提交操作了
$ git add . 
$ git commit -m "clear"
$ git push origin master  --推送到远程仓库

