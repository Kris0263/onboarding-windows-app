

## Research & Learn

### What are the differences between styling and templating in WPF?

- **Styling** defines a consistent look (e.g., colors, fonts, margins) for controls across the application. It's similar to CSS in web development.
- **Templating** allows complete customization of a control's visual structure and behavior. It changes *how* a control is rendered, not just *how it looks*.
- Styles can contain templates, but templates define the inner layout of a control, such as replacing a Button's default visuals.

### How do you define and apply styles and control templates?

- **Styles** are defined in XAML using the `<Style>` tag, often in `App.xaml` or `ResourceDictionary`:

```xml
<Style TargetType="Button">
  <Setter Property="Background" Value="LightBlue"/>
  <Setter Property="FontSize" Value="16"/>
</Style>

<ControlTemplate TargetType="Button">
  <Border Background="{TemplateBinding Background}" CornerRadius="5">
    <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
  </Border>
</ControlTemplate>
```

### How can using styles enforce consistency across your application?

Using styles centralizes UI definitions, so if you update a style (e.g., font, padding), all associated controls update automatically.  
This ensures a unified visual identity and reduces duplication, leading to a more maintainable and professional-looking application.

## Reflect on the benefits and challenges of using control templates.

###  Benefits:
- Full customization of a control's structure.
- Essential for skinnable or themeable applications.
- Allows separation of logic from UI visuals.

### Challenges:
- Requires deeper understanding of WPF's visual tree.
- Debugging custom templates can be complex.
- Can introduce inconsistencies if not documented and reused properly.

### How might templating improve the maintainability of your UI?
- Changes in control layout or behavior only need to be updated in one place.
- Encourages a modular design where visuals are swapped without affecting logic.
- Easier onboarding for new developers when templates are well-documented and reused.
