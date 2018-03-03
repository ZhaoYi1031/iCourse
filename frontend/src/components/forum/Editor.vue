<template>
  <div id="editor" class="container" v-loading.fullscreen.lock="loading" :element-loading-text="loading_text">
  <Header></Header>
    <el-row>
      <el-col :span="24">
        <el-button type="primary" icon="d-arrow-left" style="margin:20px 0px 0px 20px;width:120px" @click="return_forum_button_clicked">返回论坛
        </el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <p class="title">
          {{ course_name }}-讨论板
        </p>
        <p class="title">
          发表新贴
        </p>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4" :offset="2">
      <p class="label">
        选择帖子的类型:
      </p>
      </el-col>
      <el-col :span="18">
        <el-radio-group v-model="category" style="padding-top: 10px">
          <el-radio :label="1">问题讨论</el-radio>
          <el-radio :label="2">学习心得</el-radio>
          <el-radio :label="0">其他</el-radio>
        </el-radio-group>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4" :offset="2">
      <p class="label">
        版权说明:
      </p>
      </el-col>
      <el-col :span="18">
        <el-checkbox v-model="copyright_checked">
              我已阅读并同意遵守<el-button type="text" @click="copyright_button_clicked">《版权声明》</el-button>中的条款
        </el-checkbox>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4" :offset="2">
      <p class="label">
        标题
      </p>
    </el-col>
    </el-row>
    <el-row tpye='flex' justify="center">
      <el-col :span="20" class="input" :offset="2">
        <el-input v-model="title" placeholder="输入标题,4-30个字符">
        </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4" :offset="2">
      <p class="label">
        正文
      </p>
    </el-col>
    </el-row>
    <link href="https://cdn.quilljs.com/1.3.4/quill.snow.css" rel="stylesheet">
    <el-row type="flex" justify="center" >
      <el-col :span="20" class="editor_container">
      <quill-editor v-model="editor.content" ref="quill" class="editor" :options="editor.option" @change="on_editor_change($event)">
      </quill-editor>
    </el-col>
    </el-row>
    <el-row type="flex" justify="center" >
          <el-col :span="20" class="limit">
            <el-alert :title="note" type="info" :closable="false" show-icon v-if="!overflow">
            </el-alert>
            <el-alert :title="alert" type="error" :closable="false" show-icon v-if="overflow">
            </el-alert>
          </el-col>
        </el-row>
        <el-row type="flex">
      <el-col :span="22">
        <el-button type="primary" @click="post_submit_button_clicked" class="submit_button" size="large">
          提交
        </el-button>
      </el-col>
    </el-row>
    <el-dialog title="版权说明" :visible.sync="copyright_visible">
      <CopyrightDialog></CopyrightDialog>
      <div slot="footer">
        <center>
    <el-button type="primary" @click="copyright_visible=false">确 定</el-button>
  </center>
  </div>
    </el-dialog>
  </div>
</template>
<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header'
import $ from 'jquery'
import get_url from '../general/getUrl.js'
import CopyrightDialog from '../general/CopyrightDialog.vue'
export default {
  name: 'Editor',
  components: { Header, CopyrightDialog },
  data () {
    return {
      editor: {
        content: '',
        option: { placeholder: '帖子的正文' }
      },
      title: '',
      category: -1,
      text_limit: 10000,
      current_available_text: 10000,
      current_text_length: 0,
      dev: true,
      loading: false,
      overflow: false,
      loading_text: '发布成功，正在跳转',
      course_name: '',
      text: '',
      copyright_checked: true,
      copyright_visible: false
    }
  },
  methods: {
    copyright_button_clicked: function () {
      this.copyright_visible = true
    },
    post_submit_button_clicked: function () {
      if (!this.copyright_checked) {
        this.$message({
          showClose: true,
          message: '必须同意版权声明才能发贴',
          type: 'error'
        })
      }
      else if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          message: '请先登录',
          type: 'error'
        })
      } else if (this.title.length > 30 || this.title.length < 4) {
        this.$message({
          showClose: true,
          message: '请控制标题的长度在4-30个字符以内',
          type: 'error'
        })
      } else if (this.overflow) {
        this.$message({
          showClose: true,
          message: '正文长度最多为'+this.text_limit,
          type: 'error'
        })
      } else if (this.category === -1) {
        this.$message({
          showClose: true,
          message: '必须选择帖子的类型',
          type: 'error'
        })
      } else {
        if (this.category === 2 && this.current_text_length < 100) {
          this.message({
            showClose: true,
            message: '学习心得的正文长度需要大于100',
            type: 'error'
          })
        } else {
          this.$confirm('确认发布帖子吗？', '发布', {
            confirmButtonText: '发布',
            cancelButtonText: '取消',
            type: 'info'
          }).then(() => {
            var content = this.editor.content
            var post_data = {
              title: this.title,
              course_id: this.$route.params.course_id,
              category: this.category,
              content: content,
              editor: 0,
              intro: this.text
            }
            var post_url = get_url(this.$store.state.dev, '/post/posting/publish/')
            var _this = this
            $.ajax({
              ContentType: 'application/json; charset=utf-8',
              dataType: 'json',
              url: post_url,
              type: 'POST',
              data: post_data,
              success: function (data) {
                var code = Number(data['error'])
                if (code === 0) {
                  console.log('success')
                  _this.loading = true
                  _this.$router.push({ path: '/course/page/' + _this.$route.params.course_id + '/forum' })
                } else if (code === 1) {
                  _this.$message({
                    showClose: true,
                    type: 'error',
                    message: '发布失败'
                  })
                }
              },
              error: function () {
                _this.$message({
                  showClose: true,
                  type: 'error',
                  message: '无法链接到服务器'
                })
              }
            })
          })
        }
      }
    },
    on_editor_change: function ({ editor, html, text }) {
      this.current_text_length = text.length
      this.overflow = (text.length > this.text_limit)
      this.current_available_text = ((this.text_limit - text.length) < 0 ? 0 : (this.text_limit - text.length))
      this.text = text.substr(0, 100)
    },
    return_forum_button_clicked: function () {
      this.$router.push({ path: '/course/page/' + this.$route.params.course_id + '/forum' })
    }
  },
  computed: {
    note: function () {
      return '已经输入'+this.current_text_length+'个字符，还可以输入'+this.current_available_text+'个字符'
    },
    alert: function () {
      return '文章长度超出限制了呢，目前已经输入了:'+this.current_text_length+'个字符,超出了:'+(this.current_text_length-this.text_limit)+'个字符'
    }
  },
  mounted () {
    var post_url = get_url(this.$store.state.dev, '/course/course_info/')
    var post_data = { course_id: this.$route.params.course_id }
    var _this = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var info = data['course_info']
        _this.course_name = info.name
      },
      error: function () {
        _this.$notify({
          type: 'error',
          title: '错误',
          message: '获取课程信息失败'
        })
      }
    })
  }
}
</script>

<style type="text/css" scoped>
  .title{
    text-align: center;
    font-size: 40px;
    padding-bottom: 30px;
  }
  .limit{
    margin-top: 80px;
    margin-bottom: 20px;
  }
  .input{
    margin-top: 0px;
    margin-bottom: 20px;
  }
  .label{
    font-size: 24px;
    margin-bottom: 20px;
  }
  .editor{
    height: 500px;
    padding-bottom: 67px
  }
  .submit_button{
    float: right;
    margin-bottom: 100px;
    width: 100px;
  }
</style>