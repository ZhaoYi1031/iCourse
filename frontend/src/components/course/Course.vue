<template>
    <div id="course">
        <Header></Header>
            <el-col :span="24" class="navigator" style="margin-top: 20px">
              <el-tree :data="tree_data" :props="defaultProps" accordion @node-click="course_tree_clicked" class="course_tree">
              </el-tree>
            <section class="course_content_container">
                <div class = "grid-content bg-purple-light">
                    <el-col :span="24" class="breadcrumb-container">
                        <strong class= "course_table_title">{{ course_bread_message }}
                        </strong>
                        <el-col :span="24" class="course_content_wrapper">
                          <transition name="fade" mode="out-in">
                            <section>
                              <!-- tools bar above -->
                              <el-col :span="24" class="tools_bar_top" style="padding-bottom: 0px;">
                                <el-form :inline="true" :model="filters" >
                                  <el-form-item>
                                    <el-input type="text" v-model = "filters.name" placeholder="支持课程名、课程号" @keydown.enter.native.prevent="search_course_clicked" ></el-input>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" v-on:click="search_course_clicked" icon="search">搜索</el-button>
                                  </el-form-item>
                                  <el-form-item>
                                    <el-button type="primary" @click="add_course_clicked" icon="plus" style="float:left;" disabled=true>添加课程
                                    </el-button>
                                  </el-form-item>
                                </el-form>
                              </el-col>

                            <!-- course table -->
                            <el-col :span="24">
                            <el-table :data="courses" highlight-current-row v-loading="load_courses" style="width: auto;" height="500" stripe>
                              <el-table-column type="index" label=" 序 号 " align="center" width="100"></el-table-column>
                              <el-table-column prop="course_id" label="课程编号"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_name" label="课程名"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_academy" label="开设学院"  sortable align="center"></el-table-column>
                              <el-table-column prop="course_class" label="课程分类"  sortable align="center"></el-table-column>
                              <!--
                              <el-table-column prop="course_hours" label="学时"  sortable></el-table-column>
                            --><el-table-column prop="course_credit" label="学分"  sortable align="center"></el-table-column>
                              <el-table-column label="操作" align="center">
                              <template slot-scope="scope">
                                <el-button
                                  size="mini"
                                  @click="to_course_page(scope.$index)">进入课程</el-button>
                              </template>
                            </el-table-column>
                            </el-table>
                          </el-col>

                            <!-- tools bar beneath-->
                            <el-col :span="24" class="tools_bar_bottom">
                              <el-pagination layout="prev,pager,next" @current-change="handle_current_change" :page-size="page_size" :total="total" :current-page.sync="current_page" style="float:right;"></el-pagination>
                            </el-col>
                            </section>
                          </transition>
                        </el-col>
                    </el-col>

                </div>
            </section>
        </el-col>
</div>
</template>


<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import Header from '../general/Header'
// 请不要删除和get_url相关的行，如果你真的需要请告诉我下原因。by xindetai
import get_url from '../general/getUrl'
import college_map from '../general/collegeMap'
import $ from 'jquery'
export default {
  name: 'Course',
  components: { Header },
  data () {
    return {
      tree_data: [{
        label: '我的收藏',
        isLeaf: true
      },
      {
        label: '开设院系',
        children: [{ label: '材料科学与工程学院' },
                   { label: '电子信息工程学院' },
                   { label: '自动化科学与电气工程学院' },
                   { label: '能源与动力工程学院' },
                   { label: '航空科学与工程学院' },
                   { label: '计算机学院' },
                   { label: '机械工程及自动化学院' },
                   { label: '经济管理学院' },
                   { label: '数学与系统科学学院' },
                   { label: '生物与医学工程学院' },
                   { label: '人文社会科学学院' },
                   { label: '外国语学院' },
                   { label: '交通科学与工程学院' },
                   { label: '可靠性与系统工程学院' },
                   { label: '宇航学院' },
                   { label: '飞行学院' },
                   { label: '仪器科学与光电工程学院' },
                   { label: '物理科学与核能工程学院' },
                   { label: '法学院' },
                   { label: '软件学院' },
                   { label: '高等工程学院' },
                   { label: '高等工程学院' },
                   { label: '中法工程师学院' },
                   { label: '新媒体艺术与设计学院' },
                   { label: '化学与环境学院' },
                   { label: '思想政治理论学院' },
                   { label: '人文与社会科学高等研究' },
                   { label: '30系' },
                   { label: '32系' },
                   { label: '33系' },
                   { label: '51系' },
                   { label: '52系' },
                   { label: '56系' },
                   { label: '91系' }
        ]
      }],
      filters: {
        name: ''
      },
      total: 0, // total courses
      current_page: 1, // current page
      page_size: 10,
      load_courses: false, // v-loading
      courses: [],
      storage: [],
      course_bread_message: '查找课程',
      dev: true,
      course_class_dict: ['工程基础类', '数学与自然科学类', '语言类', '博雅类', '核心通识类', '体育类', '一般通识类', '核心专业类', '一般专业类']
    }
  },
  methods: {
    to_course_page (index) {
      this.$router.push({ path: ('/course/page/' + this.courses[index]['course_id'] + '/') })
    },
    handle_current_change (value) {
      this.current_page = value
      this.courses = []
      var len = this.storage.length < value*this.page_size ? this.storage.length % this.page_size : this.page_size

      for (var i = 0; i < len; i++) {
        this.courses.push(this.storage[(value-1)*this.page_size+i])
      }
    },
    course_tree_clicked (data, node) {
      // todo: use api to get the corresponding courses
      if (typeof (node.parent.label) !== 'undefined') {
        this.course_bread_message = node.parent.label + '->' + node.label
        this.load_courses = true
        var self = this
        if (node.parent.label === '开设院系') {
          var college_name = node.label
          var college_id = -1
          for (var id in college_map) {
            if (college_map[id] === college_name) {
              college_id = id
              break
            }
          }
          var temp1 = { 'college_id': (college_id === -1) ? node.label.substr(0, node.label.length-1) : college_id }
          var post_url = get_url(this.$store.state.dev, '/course/college_course/')
          $.ajax({
            ContentType: 'application/json; charset=utf-8',
            dataType: 'json',
            type: 'POST',
            url: post_url,
            data: temp1,
            async: false,
            success: function (data) {
              // 初始化storage和courses以及当前页数
              var info_list = data['course_info_list']
              self.storage = []
              self.total = info_list.length
              for (var i = 0; i < info_list.length; i++) {
                var college_id = info_list[i]['college_id']
                var college_info = (college_map.hasOwnProperty(college_id)) ? college_map[college_id] : college_id.toString()
                var item = {
                  'course_name': info_list[i]['name'],
                  'course_id': info_list[i]['id'],
                  'course_academy': college_info,
                  'course_hours': info_list[i]['hours'],
                  'course_credit': info_list[i]['credit'],
                  'course_class': self.course_class_dict[info_list[i]['class_id'] - 1]
                }
                self.storage.push(item)
              }
            },
            error: function () {
              self.$message({
                showClose: true,
                type: 'error',
                message: '拉取信息失败'
              })
            }
          })
          self.handle_current_change(1)
          self.load_courses = false
        }
        else if (node.parent.label === '课程类别') {
          this.$message({
            showClose: true,
            message: '课程类别暂未开放，敬请期待，当前可以使用搜索或者开设院系来查找课程~'
          })
        }
        else {
          self.$message({
            showClose: true,
            type: 'error',
            message: '结点不存在'
          })
        }
      }
      else {
        this.course_bread_message = node.label
        if (node.label === '我的收藏') {
          this.get_liked_courses()
        }
      }
    },
    search_course_clicked () {
      if (!this.filters.name) {
        this.$message.error({
          showClose: true,
          message: '搜索内容不能为空!'
        })
      }
      else {
        this.load_courses = true
        this.course_bread_message = this.filters.name
        var post_data = {
          'keyword': this.filters.name
        }
        var self = this
        var post_url = get_url(this.$store.state.dev, '/course/searching/')
        $.ajax({
          ContentType: 'application/json; charset=utf-8',
          dataType: 'json',
          url: post_url,
          type: 'POST',
          data: post_data,
          async: false,
          success: function (data) {
            self.total = data['query_list'].length
            self.storage = []
            for (var i = 0; i < data['query_list'].length; i++) {
              var course = data['query_list'][i]
              var college_id = course['college_id']
              var college_info = (college_map.hasOwnProperty(college_id)) ? college_map[college_id] : college_id.toString()
              self.storage.push({
                'course_name': course['name'],
                'course_id': course['id'],
                'course_academy': college_info,
                'course_hours': course['hours'],
                'course_credit': course['credit'],
                'course_class': course['class_id']
              })
            }
          },
          error: function () {
            self.$message({
              showClose: true,
              type: 'error',
              message: '获取课程信息列表失败'
            })
          }
        })
        self.handle_current_change(1)
        self.load_courses = false
      }
    },
    get_liked_courses () {
      this.load_courses = true
      this.course_bread_message = '我的收藏'
      var self = this
      var post_url = get_url(this.$store.state.dev, '/course/like/list/')
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        type: 'POST',
        url: post_url,
        async: false,
        success: function (data) {
          // 初始化storage和courses以及当前页数
          var info_list = data['info_list']
          self.storage = []
          self.total = info_list.length
          for (var i = 0; i < info_list.length; i++) {
            var college_id = info_list[i]['college_id']
            var college_info = (college_map.hasOwnProperty(college_id)) ? college_map[college_id] : college_id.toString()
            var item = {
              'course_name': info_list[i]['name'],
              'course_id': info_list[i]['id'],
              'course_academy': college_info,
              'course_hours': info_list[i]['hours'],
              'course_credit': info_list[i]['credit'],
              'course_class': self.course_class_dict[info_list[i]['class_id'] - 1]
            }
            self.storage.push(item)
          }
        },
        error: function () {
          self.$message({
            showClose: true,
            type: 'error',
            message: '获取课程信息列表失败'
          })
        }
      })
      self.handle_current_change(1)
      self.load_courses = false
    },
    add_course_clicked () {
      // todo: add course function
      this.$message({
        showClose: true,
        message: '功能暂未开放，敬请期待'
      })
    }
  },
  mounted () {
    this.get_liked_courses()
  }
}
</script>

<style type="text/css" scpoed>
    .tools_bar_above {
      width: auto;
      float: left;
    }
    .tools_bar_bottom {
      margin-top: 10px;
    }
    .navigator {
        font-family: Microsoft Yahei;
        display: flex;
        top: 60px;
        bottom: 0px;
        oveflow:hidden;
      }
      .course_tree {
        height: auto;
        width: auto;
        min-width: 20%;
        margin-right: 10px;
        font-family: Microsoft Yahei;
      }
      .course_table_title {
            width: 50%;
            float: left;
            color: #475669;
            margin-top: 10px;
            margin-bottom: 10px;
          }
      .content-wrapper {
          background-color: #fff;
          box-sizing: border-box;
        }
      .course_content_container{
      }
</style>