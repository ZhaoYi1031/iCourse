<template>
  <footer id="Footer" class="footer"> 
    <div align="center"><hr class="line"></div>
    <div class="footer-main">
      <p class="footer_copyright"> © 2017-2018 hotcode5</p>
      <p class="footer_link_container">
        <a href="https://github.com/Slontia/iCourse/" target="_blank" class="footer_link">Github</a>
        <a href="http://www.cnblogs.com/hotcode5/" target="_blank" class="footer_link">blog</a>
      </p>
      <p class="footer_link_container">
        <el-button type="text" size="small" @click="copyright_button_clicked" class="footer_button">版权说明</el-button>
        <el-button type="text" size="small" @click="discla_button_clicked" class="footer_button">免责声明</el-button>
      </p>
      <p class="footer_qq">QQ群: 639199158</p>
    </div>
    </div>
    <el-dialog title="版权说明" :visible.sync="copyright_visible" class="dialog">
      <CopyrightDialog></CopyrightDialog>
      <div slot="footer">
        <center>
    <el-button type="primary" @click="copyright_visible=false">确 定</el-button>
  </center>
  </div>
    </el-dialog>
    <el-dialog title="免责声明" :visible.sync="discla_visible" class="dialog">
      <DisclaDialog></DisclaDialog>
      <div slot="footer">
        <center>
    <el-button type="primary" @click="discla_visible=false">确 定</el-button>
  </center>
  </div>
    </el-dialog>
  </footer>
</template>

<script type="text/javascript">
/* eslint-disable camelcase */
import CopyrightDialog from './CopyrightDialog.vue'
import DisclaDialog from './DisclaDialog.vue'
export default {
  name: 'Footer',
  components: { CopyrightDialog, DisclaDialog },
  data () {
    return {
      copyright_visible: false,
      discla_visible: false
    }
  },
  methods: {
    copyright_button_clicked: function () {
      this.copyright_visible = true
    },
    discla_button_clicked: function () {
      this.discla_visible = true
    }
  }
}
</script>

<style type="text/css" scpoed>
  .line{
    border:none;
    border-top: 1px solid #ccc;
    margin-top: 20px;
    width: 90%;
    height: 0px;
  }
  .footer{
    position: absolute;
    font-family: Microsoft Yahei;
    background-size: 100%;
    //background-color: #58B7FF;
    width: 100%;
    height: 100px;
    text-align: center;
    margin-top: 50px;
  }
  .footer_link_container{
    margin-top: 10px;
  }
  .footer_link{
    text-decoration: none;
    margin-right: 25px;
    margin-left: 25px;
    color: #409EFF;
  }
  .footer_copyright{
    padding-top: 20px;
    color:gray;
  }
  .footer_qq{
    color:gray;
    padding-top: 10px;
    padding-bottom: 10px;
  }
  .footer_button{
    padding: 0px 0px 0px 0px;
    font-size: 16px;
  }
  .dialog{
    text-align: left;
  }
</style>
