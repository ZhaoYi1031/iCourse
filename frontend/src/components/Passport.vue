
<script type="text/javascript">
/* eslint-disable brace-style */
/* eslint-disable camelcase */
/* eslint-disable space-infix-ops */
import $ from 'jquery'
import get_url from './general/getUrl.js'
export default {
  name: 'Passport',
  mounted () {
    var code = this.$route.query.code
    var error = 1
    var username = ''
    var post_url = get_url(this.$store.state.dev, '/passport/auth/')
    var post_data = {
      'code': code
    }
    var _this = this
    $.ajax({
      ContentType: 'application/json; charset=utf-8',
      dataType: 'json',
      url: post_url,
      type: 'POST',
      data: post_data,
      async: false,
      success: function (data) {
        username = data['username']
        error = data['error']
      },
      error: function () {
        _this.$message({
          showClose: true,
          type: 'error',
          message: '验证失败'
        })
      }
    })
    if (error === 0) {
      post_url = get_url(this.$store.state.dev, '/sign/login/')
      $.ajax({
        ContentType: 'application/json; charset=utf-8',
        dataType: 'json',
        url: post_url,
        type: 'POST',
        data: {
          'username': username,
          'password': '111111111111111111111111111111'
        },
        async: false,
        success: function () {
        },
        error: function () {
          _this.$message({
            showClose: true,
            type: 'error',
            message: '登录失败'
          })
        }
      })
    }
    this.$router.push({ path: '/' })
  }
}
</script>
