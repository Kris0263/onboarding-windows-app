using System.ComponentModel;
using Databinding.Model;

namespace Databinding.ViewModel
{
    public class MainViewModel : INotifyPropertyChanged
    {
        private SampleModel _model;

        public MainViewModel()
        {
            _model = new SampleModel();
        }

        public string Message
        {
            get { return _model.Message; }
            set
            {
                if (_model.Message != value)
                {
                    _model.Message = value;
                    OnPropertyChanged(nameof(Message));
                }
            }
        }

        public event PropertyChangedEventHandler? PropertyChanged;

        protected void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}
