package com.ampd.pidar


import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_summary.*

class FinalInfoActivity : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_final_info)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        next_button.setOnClickListener { view ->
            showFinalInfo();
        }
    }


    override fun onOptionsItemSelected(item: MenuItem) = when (item.itemId) {
        android.R.id.home -> {
            onBackPressed()
            true
        }
        else -> false
    }


    private fun showFinalInfo(){
        val browserIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.adr.gov.co/servicios/Paginas/proyectos-productivos-integrales.aspx"))
        startActivity(browserIntent)
    }


}