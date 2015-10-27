//
//  ViewController.swift
//  backgroundExtensionDemo
//
//  Created by Tanzim Saqib on 10/27/15.
//  Copyright © 2015 Tanzim Saqib. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var imgView: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func onSelect(sender: UISegmentedControl) {
        switch sender.selectedSegmentIndex
        {
        case 0:
            BlurExtraLight(imgView)
        case 1:
            BlurLight(imgView)
        case 2:
            BlurDark(imgView)
        case 3:
            BlurReset()
        default:
            print("Invalid option")
        }
    }
}

