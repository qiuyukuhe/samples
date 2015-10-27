//
//  BackgroundExtension.swift
//  backgroundExtensionTest
//
//  Created by Tanzim Saqib on 10/27/15.
//  Copyright © 2015 Tanzim Saqib. All rights reserved.
//

import UIKit

extension UIViewController
{
    // Any Int value you want the views to be identified
    enum blurViewEnum: Int { case ID = -999 }
    
    func BlurExtraLight(imgView: UIImageView)
    {
        Blur(imgView, effectType: UIBlurEffectStyle.ExtraLight)
    }
    
    func BlurLight(imgView: UIImageView)
    {
        Blur(imgView, effectType: UIBlurEffectStyle.Light)
    }
    
    func BlurDark(imgView: UIImageView)
    {
        Blur(imgView, effectType: UIBlurEffectStyle.Dark)
    }
    
    func BlurReset()
    {
        for v in view.subviews
        {
            if (v.tag == blurViewEnum.ID.rawValue)
            {
                v.removeFromSuperview()
            }
        }
    }
    
    func Blur(imgView: UIImageView, effectType: UIBlurEffectStyle)
    {
        if !UIAccessibilityIsReduceTransparencyEnabled()
        {
            let effect = UIBlurEffect(style: effectType)
            let effectView = UIVisualEffectView(effect: effect)
            
            // Identify these created views with a tag for future reset
            effectView.tag = blurViewEnum.ID.rawValue
            effectView.frame = imgView.bounds   // if you want the whole view to be blurred,
                                                // use view.bounds instead
            view.addSubview(effectView)
        }
        else
        {
            self.view.backgroundColor = UIColor.blackColor()
        }
    }
}