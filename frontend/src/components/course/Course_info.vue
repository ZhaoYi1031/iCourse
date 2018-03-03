<!-- Course_info page -->
<template>
  <div id="course_info">
    <Header></Header>
    <!-- course introduction -->
    <el-row :gutter="50" class="course_introduction">
        <el-col :span="18" >
            <el-button type="primary" icon = "d-arrow-left" @click="return_course_page_clicked" style="margin-top: 20px;margin-bottom: 10px">返回课程页面</el-button>
            <el-button type="primary" @click="enter_forum_clicked"style="float:right;margin-top: 20px; margin-bottom: 10px">进入课程论坛<i class="el-icon-d-arrow-right el-icon--right"></i></el-button>
          <div class="info_card">
            <el-card class="box-card">
            <div slot="header" class = "clearfix">
              <span style="line-height:45px;text-align: left;">
                <el-row>
                  <el-col :span="24">
                    <p style="padding-top:10px;font-size: xx-large;">{{ course_name }}</p>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :span="3">
                    <el-button type="primary" @click.native="course_like" v-if="liked" >取消收藏</el-button>
                    <el-button @click.native="course_like" v-else>收 藏</el-button>
                  </el-col>
                  <el-col :span="4">
                    收藏量： {{ like_count }}
                  </el-col>
                </el-row>
              </span>
            </div>
            <div class="text item">
              授课教师: {{ teacher }}
            </div>
            <div class="text item">
              开课院系: {{ academy }}
            </div>
            <div class="text item">
              学时: {{ hours }}
            </div>
            <div class="text item">
              课程介绍: {{ intro_info }}
            </div>
            <div class="text item">
              点击: {{ visit_count }}
            </div>
            </el-card>
          </div>     
        </el-col>

      <!-- contribution rank -->
      <el-col :span="6" class = "contribution_container">
        <div class="contribution_table">
        <p style="text-align: center; padding-bottom: 10px"> 贡献度排行 </p>
        <el-table :data="contribution_data" highlight-current-row style="width: auto;" height="300">
          <el-table-column prop="contribution_username" label="用户名" align="center"></el-table-column>
          <el-table-column prop="contribution_score" label="贡献度" align="center"></el-table-column>
        </el-table>
        </div>
      </el-col>
    </el-row>
     <!-- course resource -->

     <div class = "course_resource_container">
        <el-row class="course_resource_head" style="margin-bottom: 20px;margin-top: 50px;">
          <el-col :span="24" style="margin-top: 20px">
            <el-col :span="10">
              <p style="float: left;font-size: x-large">课程资源</p>
            </el-col> 
            <el-col :span="2" :offset="9">
              <el-button type="primary" icon="view" @click="check_all_resource_clicked" style="float: right;margin-right: 20px;">
                查看全部
              </el-button>
            </el-col> 
            <el-col :span="2" :offset="1">
              <el-button type="primary" icon="upload2" @click="uploadDialogVisible=true" style="float: right;">
                上传资源
              </el-button>
            </el-col> 
          </el-col>
      </el-row>
        <el-row class = "resource_container" >
          <el-col :span="16" class="hot_resource_container">
              <p style="text-align: left;padding-bottom: 20px;font-size: large"> 热门资源 </p>
          </el-col>
            <el-col :span="8" class= "latest_resource_container" :offset="14">
              <p style="padding-bottom: 10px; font-size: large">最新资源</p>
          </el-col>
        </el-row>
        <template v-for="(i,index) in total_resource_line">
              <el-row>
                <el-col :span="7" v-bind:style="{visibility:card_data[index][0].show}">
                  <el-col :span="24">
                    <el-tooltip effect="dark" :content="card_data[index][0].title" placement="top">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,0)">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="card_data[index][0].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="19" :offset="1">
                        <el-row >
                          <p class="card_title_text">{{card_data[index][0].title}}</p>
                        <p class="card_text">
                          上传者:{{card_data[index][0].uploader}}
                        </p>
                        <p class="card_text">
                          下载量:{{card_data[index][0].frequency}}
                        </p>
                      </el-row>
                      </el-col>
                    </el-row>
                </el-button>
              </el-tooltip>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
                </el-col>

                <el-col :span="7" :offset="1" v-bind:style="{visibility:card_data[index][1].show}">
                  <el-col :span="24">
                  <el-tooltip effect="dark" :content="card_data[index][1].title" placement="top">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,1)">
                    <el-row>
                      <el-col :span="4" style="">
                        <img :src="card_data[index][1].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="19" :offset="1">
                        <el-row >
                          <p class="card_title_text">{{card_data[index][1].title}}</p>
                        <p class="card_text">
                          上传者:{{card_data[index][1].uploader}}
                        </p>
                        <p class="card_text">
                          下载量:{{card_data[index][1].frequency}}
                        </p>
                      </el-row>
                      </el-col>
                    </el-row>
                </el-button>
              </el-tooltip>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>
                </el-col>
                <el-col :span="7" :offset="1" v-bind:style="{visibility:card_data[index][2].show}">
                  <el-tooltip effect="dark" :content="card_data[index][2].title" placement="top">
                  <el-button type="text" class="card_button" @click.native="card_clicked(index,2)">
                  
                    <el-row>
                      <el-col :span="4">
                        <img :src="card_data[index][2].img" style="width: 50px; height:50px;"></img>
                      </el-col>
                      <el-col :span="19" :offset="1">
                        <el-row >
                          <p class="card_title_text">{{card_data[index][2].title}}</p>
                        <p class="card_text">
                          上传者:{{card_data[index][2].uploader}}
                        </p>
                        <p class="card_text">
                          下载量:{{card_data[index][2].frequency}}
                        </p>
                      </el-row>
                      </el-col>
                    </el-row>
                </el-button>
              </el-tooltip>
              <hr style="border: none;border-top: 1px solid rgb(241,242,244)"/>
                </el-col>

      </el-row>
    </template>
    </div>
  <el-dialog title="上传资源" :visible.sync="uploadDialogVisible">
      <el-form label-position="left">
        <el-form-item type="text" label="资源介绍" :label-width="form_label_width">
          <el-input v-model="resourceIntro" auto_complete="off" placeholder="请输入资源介绍"></el-input>
        </el-form-item>
        <el-form-item label="资源类型" :label-width="form_label_width">
          <el-radio-group v-model="resource_category">
            <el-radio :label="0">课程资料</el-radio>
            <el-radio :label="1">往年考题</el-radio>
            <el-radio :label="2">笔记/经验</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-checkbox v-model="copyright_checked">
              我已阅读并同意遵守<el-button type="text" @click="copyright_button_clicked">《版权声明》</el-button>中的条款
          </el-checkbox>
        </el-form-item>
        <el-form-item :label-width="form_label_width">
          <input type="file" value="" id="file">
        </el-form-item>     
      </el-form>  
      <span slot="footer" class="dialog-footer">
        <el-button @click="uploadDialogVisible=false">取 消</el-button>
        <el-button type="primary" @click.native="upload">上 传</el-button>
      </span>      
    </el-dialog>

  <!-- 版权说明 -->
    <el-dialog title="版权说明" :visible.sync="copyright_visible">
      <CopyrightDialog></CopyrightDialog>
      <div slot="footer">
        <center>
    <el-button type="primary" @click="copyright_visible=false">确 定</el-button>
  </center>
  </div>
    </el-dialog>

  <!-- 资源具体信息dialog -->
  <el-dialog title="资源信息" :visible.sync="dialogVisible" v-if="dialogVisible" size="small">
      <ResourceDialog></ResourceDialog>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
  </el-dialog>
  </div>

</template>

<script type="text/javascript">
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header.vue'
import DocImg from './../../assets/fileico/docx_win.png'
import PdfImg from './../../assets/fileico/pdf.png'
import PptImg from './../../assets/fileico/pptx.png'
import JpgImg from './../../assets/fileico/jpeg.png'
import ZipImg from './../../assets/fileico/zip.png'
import RarImg from './../../assets/fileico/rar.png'
import ResourceDialog from '../general/ResourceDialog.vue'
import $ from 'jquery'
// 请不要删除和get_url相关的行，如果你真的需要请告诉我下原因。by xindetai
import get_url from '../general/getUrl.js'
import college_map from '../general/collegeMap.js'
import CopyrightDialog from '../general/CopyrightDialog.vue'

export default {
  name: 'course_info',
  components: { Header, ResourceDialog, CopyrightDialog },
  beforeCreate () {
    var self = this
    var course_id = this.$route.params.course_id
    var post_url = get_url(this.$store.state.dev, '/course/course_info/')
    var postData = { 'course_id': course_id }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: postData,
      success: function (data) {
        var info = data['course_info']
        var college_id = info['college_id']
        var college_info = (college_map.hasOwnProperty(college_id)) ? college_map[college_id] : college_id.toString()
        self.course_name = info['name']
        self.teacher = undefined
        self.academy = college_info
        self.hours = info['hours']
        self.intro_info = undefined
        self.$store.state.course_code = info['course_code']
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '获取课程信息失败'
        })
      }
    })
    post_url = get_url(this.$store.state.dev, '/course/visit_count/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: postData,
      success: function (data) {
        self.visit_count = data['visit_count']
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '获取点击次数失败'
        })
      }
    })
    post_url = get_url(this.$store.state.dev, '/course/like/count/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: postData,
      success: function (data) {
        self.liked = data['liked']
        self.like_count = data['like_count']
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '获取收藏信息失败'
        })
      }
    })
  },
  data () {
    return {
      course_id: this.$route.params.course_id,
      like_count: 0,
      liked: false,
      course_name: '',
      teacher: '',
      academy: '',
      hours: '',
      intro_info: '',
      visit_count: -1,
      contribution_data: [],
      uploadDialogVisible: false,
      fileList: [],
      total_resource_line: 3,
      form_label_width: '80px',
      dialogVisible: false,
      resourceIntro: '',
      card_data: [
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }],
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }],
        [{ title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' },
         { title: '', uploader: '', frequency: '', show: 'hidden', id: '', img: '' }]
      ],
      img: { zip: ZipImg,
        pdf: PdfImg,
        ppt: PptImg,
        pptx: PptImg,
        doc: DocImg,
        docx: DocImg,
        jpg: JpgImg,
        rar: RarImg
      },
      resource_category: 0,
      copyright_checked: true,
      copyright_visible: false
    }
  },
  methods: {
    copyright_button_clicked: function () {
      this.copyright_visible = true
    },
    course_like: function () {
      var post_url = ''
      var post_data = { course_id: this.course_id }
      var _this = this
      if (!this.$store.state.is_login) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '请先登录再收藏'
        })
        return
      }
      if (this.liked) {
        post_url = get_url(this.$store.state.dev, '/course/like/cancel/')
      } else {
        post_url = get_url(this.$store.state.dev, '/course/like/add/')
      }
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: post_data,
        success: function (data) {
          if (_this.liked) {
            _this.$message({
              showClose: true,
              type: 'success',
              message: '取消成功'
            })
            _this.liked = false
            _this.like_count -= 1
          } else {
            _this.$message({
              showClose: true,
              type: 'success',
              message: '收藏成功'
            })
            _this.liked = true
            _this.like_count += 1
          }
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '收藏异常'
          })
        }
      })
    },
    course_cancel_like: function () {

    },
    return_course_page_clicked: function () {
      this.$router.push({ path: '/course/' })
    },
    upload: function () {
      if (!this.copyright_checked) {
        this.$message({
          showClose: true,
          type: 'error',
          message: '必须同意版权声明'
        })
        return
      }

      var formData = new FormData()
      var fileObj = document.getElementById('file').files[0]
      formData.append('file', fileObj)
      formData.append('name', fileObj.name)
      formData.append('only_url', false)
      formData.append('url', null)
      formData.append('intro', this.resourceIntro)
      formData.append('course_code', this.$store.state.course_code)
      var post_url = get_url(this.$store.state.dev, '/resourceUpload/')
      var _this = this
      $.ajax({
        url: post_url,
        type: 'POST',
        data: formData,
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (rdata) {
          rdata = JSON.parse(rdata)
          if (rdata['error'] === 0) {
            _this.$message({
              showClose: true,
              type: 'success',
              message: '上传成功！'
            })
          } else {
            _this.$message({
              showClose: true,
              type: 'error',
              message: '上传失败！' + rdata['error']
            })
          }
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '上传异常'
          })
        }
      })
    },
    edit_course: function () {
      this.$message({
        showClose: true,
        message: '功能暂未开放，敬请期待'
      })
    },
    submitUpload () {
      this.$refs.upload.submit()
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    check_all_resource_clicked: function () {
      this.$router.push({ path: 'resource/' })
    },
    enter_forum_clicked: function () {
      this.$router.push({ path: 'forum/' })
    },
    card_clicked (i, j) {
      this.$store.state.id = this.card_data[i][j].id
      var resourceDialogSelf = this
      var post_url = get_url(this.$store.state.dev, '/resource/information/')
      var _this = this
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        async: false,
        data: {'resource_id': resourceDialogSelf.card_data[i][j].id},
        success: function (rdata) {
          resourceDialogSelf.$store.state.name = rdata['resource_info']['name']
          post_url = get_url(_this.$store.state.dev, '/user/information/')
          $.ajax({
            url: post_url,
            type: 'POST',
            data: {id: rdata['resource_info']['upload_user_id']},
            async: false,
            success: function (data) {
              data = JSON.parse(data)
              resourceDialogSelf.$store.state.author = data['user_info']['username']
            },
            error: function () {
              _this.$message({
                showClose: true,
                type: 'error',
                message: '获取用户名失败'
              })
            }
          })
          // resourceDialogSelf.$store.state.author = rdata['resource_info']['upload_user_id']
          resourceDialogSelf.$store.state.size = rdata['resource_info']['size']
          resourceDialogSelf.$store.state.time = rdata['resource_info']['upload_time']
          resourceDialogSelf.$store.state.intro = rdata['resource_info']['intro']
          resourceDialogSelf.$store.state.url = rdata['resource_info']['url']
          resourceDialogSelf.dialogVisible = true
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '获取资源信息失败'
          })
        }
      })
    }
  },
  mounted () {
    var course_id = this.$route.params.course_id

    // latest resource
    var post_data = { 'course_id': course_id, 'number': this.total_resource_line }
    var self = this
    var post_url = get_url(this.$store.state.dev, '/resource/latest/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var pos = 2 // pos of latest resource
        var info = data['result']
        for (var i = 0; i < info.length; i++) {
          self.card_data[i][pos].title=info[i]['name']
          self.card_data[i][pos].uploader=info[i]['username']
          self.card_data[i][pos].frequency=info[i]['download_count']
          self.card_data[i][pos].id = info[i]['resource_id']
          self.card_data[i][pos].show = 'visible'
          var name = info[i]['name'].toLowerCase()
          for (var t in self.img) {
            var temp = '.'+t+'$'
            var reg = new RegExp(temp)
            if (reg.test(name)) {
              self.card_data[i][pos].img = self.img[t]
              break
            }
          }
        }
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '拉取最新资源列表失败'
        })
      }
    })
    // hot resource
    post_data = { 'course_id': course_id, 'number': this.total_resource_line*2 }
    post_url = get_url(this.$store.state.dev, '/course/resource/download/most/info/')
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      success: function (data) {
        var info = data['info_list']
        for (var i = 0; i < info.length; i++) {
          var col = Math.floor(i % 2)
          var row = Math.floor(i / 2)
          self.card_data[row][col].title=info[i]['name']
          self.card_data[row][col].uploader=info[i]['username']
          self.card_data[row][col].frequency=info[i]['download_count']
          self.card_data[row][col].id = info[i]['resource_id']
          self.card_data[row][col].show = 'visible'
          var name = info[i]['name'].toLowerCase()
          for (var t in self.img) {
            var temp = '.'+t+'$'
            var reg = new RegExp(temp)
            if (reg.test(name)) {
              self.card_data[row][col].img = self.img[t]
              break
            }
          }
        }
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '拉取热门资源列表失败'
        })
      }
    })
    // course contribution
    var post_url1 = get_url(this.$store.state.dev, '/course/contri/')
    var post_data1 = { course_id: this.$route.params.course_id }
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url1,
      type: 'POST',
      data: post_data1,
      success: function (data) {
        var contri_list = data['contri_list']
        if (contri_list) {
          for (var i = 0; i < contri_list.length; i++) {
            var temp = {}
            temp.contribution_score = contri_list[i].contri
            temp.contribution_username = contri_list[i].username
            self.contribution_data.push(temp)
          }
        }
      },
      error: function () {
        self.$message({
          showClose: true,
          type: 'error',
          message: '无法连接到服务器'
        })
      }
    })
  }
}
</script>


<style type="text/css" scoped>
  .course_introduction{
    margin-top: 10px;
    padding-left: 20px;
    height: 100%;
    width: 100%;
  }
  .contribution_container{
    position:absolute;
    left:75%;
    margin-left: 10px;
  }
  .contribution_table{
    margin-bottom: 50px;
  }
  .item{
    padding-bottom: 5px;
  }
  .course_resource_container{
    position:absolute;
    top:400px;
    margin-top: 40px;
    padding-left: 20px;
    width: 71%;
  }
  .resource_container{
    width:auto;
  }
  .hot_resource_container{
    width:auto;
  }
  .latest_resource_container{
    width: auto;
  }
  .card_title_text:hover{
    color: #58B7FF;
  }
  .card_button{
    padding-top:0px;
    margin-top:0px;
    border:0px;
    width:100%;
    height:100%;
    text-align:left;
  }
  .card_title_text{
    padding-bottom: 10px;
    word-break: break-all;
    word-wrap: break-word;
    white-space: pre-wrap;
    color: black;
  }
  .card_text{
    color: grey;
  }
</style>