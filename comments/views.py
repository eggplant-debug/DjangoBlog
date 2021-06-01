from django.shortcuts import render

# Create your views here.
from blog.models import Post
from django.shortcuts import get_object_or_404,redirect,render
from django.views.decorators.http import require_POST

from .forms import CommentForm

from django.contrib import messages

@require_POST
def comment(request,post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post=get_object_or_404(Post,pk=post_pk)
    # django 将用户提交的数据封装在request.POST中，这是一个类字典对象
    # 我们利用这些数据构造了COmmentForm 的实例，这样就生成了一个绑定了用户信息的表单。

    form=CommentForm(request.POST)

    # 当调用 form.is_valid() 方法时，django 自动帮我们检查表单的数据是否符合格式要求。
    if form.is_valid():
        # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
        # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
        comment=form.save(commit=False)

        # 将评论和被评论的文章关联起来
        comment.post=post

        #最终将评论数据保存到数据库中， 调用模型实例的save方法
        comment.save()

        messages.add_message(request,messages.SUCCESS,'评论发表成功',extra_tags='success')


        #重定向到post 的详情界面，实际上当redirect 函数接收一个模型的实例时，它会调用这个模型实例的get_absolute_url 方法，
        # 然后重定向到get_absolute_url 方法返回的url.

        return redirect(post)

    # 检查到数据不合法，我们渲染一个预览界面，用于展示表单的错误
    # 注意这里被评论的文章post 也传给了末班，因为我们需要根据post来生成表单的提交地址

    context={
        'post':post,
        'form':form,
    }
    messages.add_message(request,messages.ERROR,'评论发表失败!请修改表单中的错误后再提交',extra_tags='danger')
    return  render(request,'comments/preview.html',context=context)


